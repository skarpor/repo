from django.contrib import admin, messages
from import_export.admin import ImportExportModelAdmin

from .models import Warehouse, Category, Brand, Item, Order, Apply
from .resources import BrandResource,CategoryResource,WarehouseResource,ItemResource

admin.site.site_header = '后台管理'
admin.site.site_title = '管理后台'
# admin.site.index_title = '欢迎来到仓库管理'



@admin.register(Warehouse)
class WarehouseAdmin(ImportExportModelAdmin):  # admin.ModelAdmin 基础功能，ImportExportModelAdmin 导入导出
    list_display = ('name', 'location', 'description')
    # search_fields = ('name', 'part_number')
    # resource_class = SparePartModelResource # 后台管理配置导入导出按钮
    resource_class = WarehouseResource # 后台管理配置导入导出按钮
    list_per_page = 10  # 每页显示50条记录


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):  # admin.ModelAdmin 基础功能，ImportExportModelAdmin 导入导出
    list_display = ('name', 'description')
    # search_fields = ('name', 'part_number')
    resource_class = CategoryResource # 后台管理配置导入导出按钮
    list_per_page = 10  # 每页显示50条记录


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):  # admin.ModelAdmin 基础功能，ImportExportModelAdmin 导入导出
    list_display = ('name', 'description')
    # search_fields = ('name', 'part_number')
    resource_class = BrandResource  # 后台管理配置导入导出按钮
    list_per_page = 10  # 每页显示50条记录


@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):  # admin.ModelAdmin 基础功能，ImportExportModelAdmin 导入导出
    list_display = (
    'name', 'category', 'brand', 'sn', 'update_time', 'warehouse', 'status', 'out_time', 'user', 'usage',)
    search_fields = ('name', 'category__name', 'brand__name', 'sn','user', 'usage')
    list_filter = ('category__name', 'brand__name', 'status', 'warehouse__name')
    # resource_class = SparePartModelResource # 后台管理配置导入导出按钮
    list_per_page = 10  # 每页显示50条记录
    resource_class = ItemResource # 后台管理配置导入导出按钮

    def save_model(self, request, obj, form, change):  # 强制变更为操作人
        obj.user = request.user.username  # 设置当前用户为创建者
        super().save_model(request, obj, form, change)


# @admin.register(Order)
# class OrderAdmin(ImportExportModelAdmin):
#     list_display = ('name', 'item','option','update_time', 'user', 'manager_user')
#     list_filter = ('option','user')
#     search_fields = ('name', 'item__name', 'item__category__name', 'item__brand__name', 'item__sn', 'item__warehouse__name','description')
#     # date_hierarchy = 'record_date'
#     # resource_class = ImportExportRecordModelResource # 后台管理配置导入导出按钮
#     list_per_page = 10  # 每页显示50条记录
#     def save_model(self, request, obj, form, change):
#         # print(change)
#         print(request.user.username)
#         obj.manager_user = request.user.username  # 设置当前用户为创建者
#         super().save_model(request, obj, form, change)
@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ('name', 'item', 'option', 'create_time', 'update_time', 'user', 'manager_user', 'status')
    list_filter = ('option', 'user', 'status', 'manager_user')
    search_fields = (
    'name', 'item__name', 'item__category__name', 'item__brand__name', 'item__sn', 'user__username', 'description')
    actions = ['approve_requests', 'reject_requests']
    list_per_page = 10  # 每页显示50条记录

    def save_model(self, request, obj, form, change):
        if obj.option == obj.item.status:
            messages.set_level(request, messages.ERROR)  # 设置消息级别为错误
            self.message_user(request, "申请失败，当前物品出入库状态未变更", level='error')
            return
        elif obj.item.status == "pending" and obj.option == "export":
            messages.set_level(request, messages.ERROR)  # 设置消息级别为错误
            self.message_user(request, "申请失败，当前物品未入库", level='error')
            return
        else:
            messages.set_level(request, messages.INFO)  # 设置消息级别
        obj.user = request.user.username  # 设置当前用户为创建者
        # print(dir(obj))
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # 设置默认过滤条件，例如默认显示状态为'激活'的对象
        return qs.filter()  # 这里可以根据需要调整默认条件

    def approve_requests(self, request, queryset):
        if not request.user.has_perm('yourapp.can_approve'):
            self.message_user(request, "无权操作", level='error')
            return

        for approval_request in queryset:
            if approval_request.status != "pending":
                self.message_user(request, "已通过或驳回的请求无法进行操作", level='error')
                return
            approval_request.status = 'approved'
            approval_request.manager_user = request.user.username
            print(dir(approval_request))
            # approval_request.order_set.manager_user=request.user.username
            # approval_request.order_set.save()
            approval_request.item.status = approval_request.option
            approval_request.item.save()
            approval_request.save()
        self.message_user(request, "已批准所选请求。")

    def reject_requests(self, request, queryset):
        if not request.user.has_perm('yourapp.can_approve'):
            self.message_user(request, "无权操作", level='error')
            return

        for approval_request in queryset:
            approval_request.status = 'rejected'
            approval_request.manager_user = request.user.username
            approval_request.save()
        self.message_user(request, "已驳回所选请求。")

    approve_requests.short_description = "通过所选的 出入库请求"
    reject_requests.short_description = "驳回所选的 出入库请求"
