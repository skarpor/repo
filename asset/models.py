from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(primary_key=True,max_length=200, verbose_name="类别名称",unique=True)
    description = models.TextField(blank=True, verbose_name="描述")
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "设备类别"
        verbose_name_plural = "设备类别"


class Brand(models.Model):
    name = models.CharField(primary_key=True,max_length=100, verbose_name="品牌名称",unique=True)
    description = models.TextField(blank=True,verbose_name="描述")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "设备品牌"
        verbose_name_plural = "设备品牌"
class Network(models.Model):
    name = models.CharField(primary_key=True,max_length=100, verbose_name="网络类型",unique=True)
    description = models.TextField(blank=True,verbose_name="描述")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "网络类型"
        verbose_name_plural = "网络类型"
class Operation_system(models.Model):
    name = models.CharField(primary_key=True,max_length=100, verbose_name="操作系统",unique=True)
    description = models.TextField(blank=True,verbose_name="描述")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "操作系统"
        verbose_name_plural = "操作系统"
class Department(models.Model):
    name = models.CharField(primary_key=True,max_length=100, verbose_name="部门名称",unique=True)
    description = models.TextField(blank=True,verbose_name="描述")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门"


class Item(models.Model):
    item_id = models.AutoField(primary_key=True, verbose_name="序号")  # ID
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name="部门名称")
    location = models.CharField(max_length=100, verbose_name="存放区域", blank=True)
    user = models.CharField(max_length=100,verbose_name="使用人",blank=True)
    device_code = models.CharField(max_length=100, verbose_name="设备编号",unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="设备类型")
    network = models.ForeignKey(Network, on_delete=models.PROTECT, verbose_name="接入网络")
    operation_system = models.ForeignKey(Operation_system, on_delete=models.PROTECT, verbose_name="操作系统")
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,verbose_name="品牌")
    device_model = models.CharField(max_length=100, verbose_name="设备型号", blank=True, null=True)
    sn = models.CharField(max_length=100, verbose_name="设备序列号",blank=True, null=True)
    ip = models.CharField(max_length=100, verbose_name="IP地址",blank=True, null=True)
    mac = models.CharField(max_length=100, verbose_name="MAC地址",blank=True, null=True)
    status = models.CharField(max_length=10,  choices=(('inuse', '在用'),('unuse', '未在用')), verbose_name="使用状态",default='inuse', blank=True,)
    owner=models.CharField(max_length=100,verbose_name="资产所属",blank=True,null=True)
    tag=models.CharField(max_length=100,verbose_name="资产标签号",blank=True,null=True)
    net_pointer=models.CharField(max_length=100,verbose_name="信息点",blank=True,null=True)
    telephone=models.CharField(max_length=100,verbose_name="座机号",blank=True,null=True)
    update_time = models.DateTimeField(default=timezone.now,verbose_name="修改时间",blank=True)
    operator = models.ForeignKey(User,default=User,on_delete=models.PROTECT,verbose_name="操作人",blank=True,null=True)
    description = models.TextField(blank=True,verbose_name="描述",null=True)       # 商品描述
    class Meta:
        verbose_name = "台账信息"
        verbose_name_plural = "台账信息"
    def __str__(self):
        return f"{self.department} - {self.user} - ({self.location}) - ({self.device_code})"

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
        else:
            pass
        super().save(*args, **kwargs)  # 先保存记录
        # print(self.user,self.status)
        # spare_part.save()  # 再保存备件
