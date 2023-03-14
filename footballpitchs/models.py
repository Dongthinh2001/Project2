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
    class PitchStatus (models.TextChoices):
        EMPTY = 'EM', _('Empty')
        BOOKED = 'BO', _('Booked')
    id_pitch = models.AutoField(primary_key=True)
    name_pitch = models.CharField(max_length=50)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='5')
    price = models.PositiveIntegerField()
    
