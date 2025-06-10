from import_export import resources
from .models import Item, Brand, Category, Apply, Warehouse


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand
        # 如果你的模型没有id字段，或者你希望在导入时忽略它，可以在Meta类中使用exclude属性。例如：
        # exclude = ('brand_id',)  # 如果不需要id字段
        import_id_fields = ['name']
        fields = ('name', 'description')


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        # 如果你的模型没有id字段，或者你希望在导入时忽略它，可以在Meta类中使用exclude属性。例如：
        # exclude = ('brand_id',)  # 如果不需要id字段
        import_id_fields = ['name']
        fields = ('name', 'description')


class WarehouseResource(resources.ModelResource):
    class Meta:
        model = Warehouse
        # 如果你的模型没有id字段，或者你希望在导入时忽略它，可以在Meta类中使用exclude属性。例如：
        # exclude = ('brand_id',)  # 如果不需要id字段
        import_id_fields = ['name']
        fields = ('name', 'location', 'description')


class ItemResource(resources.ModelResource):
    class Meta:
        model = Item
        # 如果你的模型没有id字段，或者你希望在导入时忽略它，可以在Meta类中使用exclude属性。例如：
        exclude = ('item_id',)  # 如果不需要id字段
        import_id_fields = ['sn',]
        fields = ('code', 'name', 'category', 'brand','model', 'sn', 'specs','update_time', 'warehouse', 'location', 'status', 'out_time', 'user', 'usage', 'destination', 'description')
