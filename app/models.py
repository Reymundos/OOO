from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Shopping(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    amount = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
