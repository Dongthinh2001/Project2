from django.db import models
from orders.models import Order
from equipments.models import Equipment
# Create your models here.
class OrderDetail (models.Model):
    id_orderdetail = models.AutoField(primary_key=True)
    id_order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    id_equipment = models.ForeignKey(Equipment,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(max_length=3)