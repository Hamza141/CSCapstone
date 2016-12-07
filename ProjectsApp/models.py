"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models
from CompaniesApp.models import Company
from GroupsApp.models import Group
import datetime


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    yearsOfExperience = models.IntegerField(default=None)
    programmingLanguage = models.CharField(max_length=20,default=None)
    speciality = models.CharField(max_length=20,default=None)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,default=None)
    created_at = models.DateField()
    assigned_to = models.ForeignKey(Group, on_delete=models.CASCADE,default=None,null=True)

    # updated_at = models.DateTimeField('date updated')


    # TODO Task 3.5: Add field for company relationship
    # TODO Task 3.5: Add fields for project qualifications (minimum required: programming language, years of experience, speciality)

    def __str__(self):
        return self.name
