from datetime import datetime
from django.db import models

from accounts.models import Account

# Create your models here.
class Post(models.Model):
    id_post = models.AutoField(primary_key= True)
    user_name = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.now)
    match_time = models.DateTimeField(null=False,default=None)
    content = models.CharField(max_length=256)