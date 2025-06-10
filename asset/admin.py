from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Category, Brand, Item,Operation_system,Department,Network
from .resources import BrandResource,CategoryResource,ItemResource,DepartmentResource,Operation_systemResource,NetworkResource

admin.site.site_header = '后台管理'
admin.site.site_title = '管理后台'
# admin.site.index_title = '欢迎来到仓库管理'

@admin.register(Operation_system)
class Operation_systemAdmin(ImportExportModelAdmin):  # admin.ModelAdmin 基础功能，ImportExportModelAdmin 导入导出
    list_display = ('name', 'description')
    # search_fields = ('name', 'part_number')
    resource_class = Operation_systemResource # 后台管理配置导入导出按钮
    list_per_page = 10  # 每页显示50条记录
@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):  # admin.ModelAdmin 基础功能，ImportExportModelAdmin 导入导出
    list_display = ('name', 'description')
    # search_fields = ('name', 'part_number')
    resource_class = DepartmentResource # 后台管理配置导入导出按钮
    list_per_page = 10  # 每页显示50条记录
@admin.register(Network)
class NetworkAdmin(ImportExportModelAdmin):  # admin.ModelAdmin 基础功能，ImportExportModelAdmin 导入导出
    list_display = ('name', 'description')
    # search_fields = ('name', 'part_number')
    resource_class = NetworkResource # 后台管理配置导入导出按钮
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
    'location','user','device_code','tag','network','ip','operation_system', 'category', 'brand', 'status', 'operator','update_time',)
    search_fields = ('location','user','ip','device_code', 'sn','tag')
    list_filter = ('network','operation_system','category', 'brand', 'status')
    # resource_class = SparePartModelResource # 后台管理配置导入导出按钮
    list_per_page = 10  # 每页显示50条记录
    # resource_class = ItemResource # 后台管理配置导入导出按钮
    resource_classes=[ItemResource,]
    readonly_fields = ('operator',)
    def save_model(self, request, obj, form, change):  # 强制变更为操作人
        # print(request.user.username)
        # print(dir(obj))

        obj.operator = request.user  # 设置当前用户为创建者
        super().save_model(request, obj, form, change)
