"""GroupsApp Models

Created by Naman Patwari on 10/10/2016.
"""
from django.db import models

from AuthenticationApp.models import MyUser


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    members = models.ManyToManyField(MyUser)
    pro = models.CharField(max_length=200, default=None, null=True)
    comp = models.CharField(max_length=200, default=None, null=True)


    def __str__(self):
        return self.name
