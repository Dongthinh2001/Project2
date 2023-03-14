from django.db import models

from accounts.models import Account
from footballpitchs.models import FootballPitch
from datetime import datetime

# Create your models here.


class Order (models.Model):
    class OrderStatus (models.TextChoices):
        WAITING = "WAI", _('Waiting')
        CONFIRMED = "CON", _('Confirmed')
    id_order = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    id_pitch = models.ForeignKey(FootballPitch, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(default=datetime.now)
    ordered_date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=64,choices=OrderStatus.choices,default=OrderStatus.WAITING)
