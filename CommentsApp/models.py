from django.db import models

from AuthenticationApp.models import MyUser
from GroupsApp.models import Group


# Create your models here.
class Comment(models.Model):
    time = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=500)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    comment_by = models.ForeignKey(MyUser, null=True)
