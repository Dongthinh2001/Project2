from django.db import models

# Create your models here.
class Equipment (models.Model):
    id_equipment = models.AutoField(primary_key=True)
    name_equipment = models.CharField(max_length=32)
    price_equipment = models.DecimalField(max_digits=16,decimal_places=3)
    description = models.CharField(max_length=256,null=True)