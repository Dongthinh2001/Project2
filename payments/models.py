from django.db import models
from orders.models import Order
from datetime import datetime
# Create your models here.
class Payment (models.Model):
    class PaymentStatus (models.TextChoices):
        UPAID = "UP",_('Upaid')
        DEPOSIT = "DE",_('Deposit')
    id_payment = models.AutoField(primary_key=True)
    id_order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    deposit_date = models.DateTimeField(default=datetime.now)
    total = models.DecimalField(max_digits=32,decimal_places=3)
    status = models.CharField(max_length=32,choices=PaymentStatus.choices,default=PaymentStatus.UPAID)