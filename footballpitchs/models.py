from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
SIZE_CHOICES = (
    ('5', '5'),
    ('7', '7'),
    ('9', '9'),
    ('11', '11'),
)


class FootballPitch (models.Model):
    class TimeSlot (models.TextChoices):
        TIME_1 = "T1", _('8h-9h30')
        TIME_2 = "T2", _('9h30-11h')
        TIME_3 = "T3", _('13h-14h30')
        TIME_4 = "T4", _('14h30-16h')
        TIME_5 = "T5", _('16h-17h30')
        TIME_6 = "T6", _('17h30-19h')
        TIME_7 = "T7", _('19h-20h30')
        TIME_8 = "T8", _('20h30-22h')

    class PitchStatus (models.TextChoices):
        EMPTY = 'EM', _('Empty')
        BOOKED = 'BO', _('Booked')
    id_pitch = models.AutoField(primary_key=True)
    name_pitch = models.CharField(max_length=50)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='5')
    time_slot = models.CharField(
        max_length=20, choices=TimeSlot.choices, default=None)
    price = models.PositiveIntegerField()
    status = models.CharField(
        max_length=50, choices=PitchStatus.choices, default=PitchStatus.EMPTY)
