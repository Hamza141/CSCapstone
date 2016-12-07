"""ProjectsApp Models

Created by Harris Christiansen on 10/02/16.
"""
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    #yearsOfExperience = models.IntegerField()
   # programmingLanguage = models.CharField(max_length=20)
    #speciality = models.CharField(max_length=20)
    # company_t = models.CharField(max_length=30)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

    # TODO Task 3.5: Add field for company relationship
    # TODO Task 3.5: Add fields for project qualifications (minimum required: programming language, years of experience, speciality)

    def __str__(self):
        return self.name