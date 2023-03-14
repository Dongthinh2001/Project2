from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Account(models.Model):
    class RoleEnum (models.TextChoices):
        ADMIN = "AD", _('Admin')
        CUSTOMER = "CU", _('Customer')

    user_name = models.CharField(max_length=100, primary_key=True)
    full_name = models.CharField(max_length=200, null = False)
    password = models.CharField(max_length=100,null=False)
    phone = models.CharField(max_length=50,unique=True,null=False)
    date_of_registration = models.DateField('Date of Registration')
    image_account = models.BinaryField()
    role = models.CharField(
        max_length=2, choices=RoleEnum.choices, default=RoleEnum.CUSTOMER)