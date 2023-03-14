# from abc import _FuncT
from django.db import models

from accounts.models import Account
from footballpitchs.models import FootballPitch
from datetime import datetime
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Order (models.Model):
    class TimeSlot (models.TextChoices):
        TIME_1 = "T1", _('8h-9h30')
        TIME_2 = "T2", _('9h30-11h')
        TIME_3 = "T3", _('13h-14h30')
        TIME_4 = "T4", _('14h30-16h')
        TIME_5 = "T5", _('16h-17h30')
        TIME_6 = "T6", _('17h30-19h')
        TIME_7 = "T7", _('19h-20h30')
        TIME_8 = "T8", _('20h30-22h')
    class OrderStatus (models.TextChoices):
        WAITING = "WAI", _('Waiting')
        CONFIRMED = "CON", _('Confirmed')
    id_order = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    id_pitch = models.ForeignKey(FootballPitch, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(default=datetime.now)
    ordered_date = models.DateTimeField(default=datetime.now)
    time_slot = models.CharField(
        max_length= 64, choices= TimeSlot.choices, default=TimeSlot.TIME_1
    )
    status = models.CharField(
        max_length=64, choices=OrderStatus.choices, default=OrderStatus.WAITING)
