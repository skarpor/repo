from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User


class Warehouse(models.Model):
    """
    仓库：bzzx仓库、gj仓库
    """
    # warehouse_id = models.AutoField(primary_key=True, verbose_name="仓库ID")  # 仓库ID
    name = models.CharField(primary_key=True,max_length=200, verbose_name="仓库名称",unique=True)  # 仓库ID
    location = models.CharField(max_length=255, verbose_name="仓库地址")        # 仓库位置
    # capacity = models.IntegerField()                    # 仓库容量
    description = models.TextField(blank=True, verbose_name="描述")
    def __str__(self):
        return f"{self.name} - {self.location}"
    class Meta:
        verbose_name = "仓库管理"
        verbose_name_plural = "仓库管理"
class Category(models.Model):
    """
    类别: 如 内存条、服务器、PC主机等
    """
    # category_id = models.AutoField(primary_key=True, verbose_name="类别ID")
    name = models.CharField(primary_key=True,max_length=100,verbose_name="物品类别",unique=True)
    description = models.TextField(blank=True,verbose_name="描述")       # 商品描述
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "物品类别"
        verbose_name_plural = "物品类别"

class Brand(models.Model):
    # brand_id = models.AutoField(primary_key=True, verbose_name="品牌ID")  # ID
    name = models.CharField(primary_key=True,max_length=100, verbose_name="品牌名称",unique=True)
    # model = models.CharField(max_length=100, verbose_name="型号")
    description = models.TextField(blank=True,verbose_name="描述")
    def __str__(self):
        return self.name # f"{self.name} - {self.model}"
    class Meta:
        verbose_name = "物品品牌"
        verbose_name_plural = "物品品牌"

class Item(models.Model):
    item_id = models.AutoField(primary_key=True, verbose_name="物品ID")  # ID
    code = models.CharField(max_length=100, verbose_name="物品编码")          # 商品名称
    name = models.CharField(max_length=100, verbose_name="物品名称")          # 商品名称
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="物品类别")
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,verbose_name="品牌")
    model = models.CharField(default=brand.name,max_length=100,verbose_name="型号")
    sn = models.CharField(max_length=100, verbose_name="序列号",unique=True)
    specs = models.CharField(max_length=100, verbose_name="规格描述",blank=True)
    update_time = models.DateTimeField(default=timezone.now,verbose_name="入库时间",blank=True)
    warehouse = models.ForeignKey(Warehouse,on_delete=models.CASCADE,verbose_name="仓库信息")
    location = models.CharField(max_length=100,verbose_name="存放位置",blank=True,null=True)
    status = models.CharField(max_length=10,  choices=(('pending', '待入库'),('import', '入库'), ('export', '出库')), verbose_name="入库/出库", blank=True,)
    out_time = models.DateTimeField(verbose_name="出库时间", blank=True,null=True)
    user = models.CharField(max_length=100,verbose_name="操作人",blank=True)
    usage = models.TextField(blank=True,verbose_name="用途",null=True)
    destination = models.TextField(blank=True,verbose_name="去向",null=True)
    description = models.TextField(blank=True,verbose_name="描述",null=True)       # 商品描述
    class Meta:
        verbose_name = "仓库物品"
        verbose_name_plural = "仓库物品"
    def __str__(self):
        return f"{self.name} - {self.brand} - {self.category} - {self.sn} - {self.warehouse}"

    def save(self, *args, **kwargs):
        # 在保存记录时更新备件的库存
        if self.pk is not None:
            pass
            # orig = Item.objects.get(pk=self.pk)
            # if orig.status !=self.status:
            #     order = Order(
            #         name="系统自动生成",
            #         item=self,
            #         option=self.status,
            #         apply=self.,
            #         user=self.user,
            #         description="出入库状态变更时自动生成",
            #     )
            #     order.save()
            if self.status == "export":
                if not self.out_time:
                    self.out_time = timezone.now()
                self.location="已出库"
        else:
            self.status="pending"
            if not self.update_time:
                self.update_time=timezone.now()
        super().save(*args, **kwargs)  # 先保存记录
        # print(self.user,self.status)
        # spare_part.save()  # 再保存备件


class Apply(models.Model):
    apply_id = models.AutoField(primary_key=True, verbose_name="申请ID")  # ID
    name = models.CharField(max_length=100, verbose_name="申请名称")
    # model = models.CharField(max_length=100, verbose_name="型号")
    item = models.ForeignKey(Item,on_delete=models.CASCADE,verbose_name="物品信息")
    option = models.CharField(max_length=10,choices=(('import', '入库'), ('export', '出库')), verbose_name="入库/出库")
    status = models.CharField(max_length=10,choices=(('pending', '待审批'), ('approved', '已通过'), ('rejected', '已驳回')), verbose_name="审批状态",blank=True)
    user = models.CharField(max_length=100,verbose_name="申请人",blank=True)
    manager_user=models.CharField(max_length=100, editable=False,verbose_name="审批人",blank=True,null=True,)  # 设置为不可编辑
    create_time = models.DateTimeField(default=timezone.now,blank=True,verbose_name="申请日期")
    update_time = models.DateTimeField(verbose_name="审批日期",blank=True,null=True)
    description = models.TextField(blank=True,verbose_name="描述")       # 商品描述
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # 在保存记录时更新备件的库存
        if self.pk is not None:
            # orig = Apply.objects.get(pk=self.pk)
            # orig = self.item
            # self.item.
            # print(self.item.status)
            # if self.status=="approved" and orig.item.status != self.option:
            #     order = Order(
            #         name="系统自动生成",
            #         item=self.item,
            #         option=self.option,
            #         apply=self,
            #         user=self.user,
            #         manager_user=self.manager_user,
            #         update_time=timezone.now(),
            #         description="出入库审批状态变更时自动生成",
            #     )
            #     order.save()
            self.update_time=timezone.now()
            if self.option == "export":
                self.item.out_time = timezone.now()

        else:
            self.status="pending"
            # self.user=self.item.user
        super().save(*args, **kwargs)  # 先保存记录

    class Meta:
        verbose_name = "出入库申请"
        verbose_name_plural = "出入库申请"
        permissions = [
            ("can_approve", "Can approve requests"),
        ]


class Order(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name="出入库ID")  # ID
    name = models.CharField(max_length=100, verbose_name="出入库名称")
    # model = models.CharField(max_length=100, verbose_name="型号")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="物品信息")
    apply = models.ForeignKey(Apply, on_delete=models.CASCADE, verbose_name="出入库申请")
    option = models.CharField(max_length=10, default="import", choices=(('import', '入库'), ('export', '出库')),
                              verbose_name="入库/出库")

    user = models.CharField(max_length=100, verbose_name="申请人")
    manager_user = models.CharField(max_length=100, verbose_name="审批人", blank=True,
                                    null=True, )  # 设置为不可编辑
    update_time = models.DateTimeField(default=timezone.now, verbose_name="变更日期")
    description = models.TextField(blank=True, verbose_name="描述")  # 商品描述

    class Meta:
        verbose_name = "出入库记录"
        verbose_name_plural = "出入库记录"

    def save(self, *args, **kwargs):
        # 在保存记录时更新备件的库存
        if self.pk is not None:
            orig = Order.objects.get(pk=self.pk)
            item = self.item
            if orig.option != self.option:
                item.status = self.option
                # item.update_time = timezone.now()
                # item.user = self.user
            item.save()
        self.user=self.apply.user
        self.manager_user=self.apply.manager_user
        super().save(*args, **kwargs)  # 先保存记录
        # 入库，若当前为出库状态，则生成记录
        # 出库，记录并相关item信息
