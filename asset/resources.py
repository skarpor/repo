from import_export import resources
from .models import Category, Brand, Item,Operation_system,Department,Network


class Operation_systemResource(resources.ModelResource):
    class Meta:
        model = Operation_system
        import_id_fields = ['name']
        fields = ('name', 'description')
class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department
        import_id_fields = ['name']
        fields = ('name', 'description')
class NetworkResource(resources.ModelResource):
    class Meta:
        model = Network
        import_id_fields = ['name']
        fields = ('name', 'description')
class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand
        import_id_fields = ['name']
        fields = ('name', 'description')


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        # exclude = ('brand_id',)  # 如果不需要id字段
        import_id_fields = ['name']
        fields = ('name', 'description')


class ItemResource(resources.ModelResource):
    class Meta:
        model = Item
        skip_unchanged = True
        report_skipped = False
        # 如果你的模型没有id字段，或者你希望在导入时忽略它，可以在Meta类中使用exclude属性。例如：
        exclude = ('item_id','operator','update_time')  # 如果不需要id字段
        import_id_fields = ('device_code',)
        # fields = ('code', 'name', 'category', 'brand','model', 'sn', 'specs','update_time', 'warehouse', 'location', 'status', 'out_time', 'user', 'usage', 'destination', 'description')
        fields = ('department','location' , 'user', 'device_code', 'category', 'network','operation_system' , 'brand', 'device_model',
                  'sn', 'ip', 'mac', 'status', 'owner', 'tag', 'net_pointer', 'telephone','description')
