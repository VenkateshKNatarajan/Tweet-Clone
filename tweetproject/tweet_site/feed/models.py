from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class tweet(models.Model):
    text = models.CharField(max_length=420,default =" ")
    datetime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User,on_delete=models.CASCADE)