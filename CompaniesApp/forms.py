"""
CompaniesApp Forms

Created by Jacob Dunbar on 10/3/2016.
"""
from django import forms

class CompanyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    photo = forms.ImageField(label='Photo');
    description = forms.CharField(label='Description', max_length=300)
    website = forms.CharField(label='Website', max_length=300)

class ProjectForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    description = forms.CharField(label='Description', max_length=300)
    assignedTo = forms.CharField(label='Assigned To', max_length=100)
    yearsOfExperience = forms.NumberInput()
    programmingLanguage = forms.CharField(label='Programming Language', max_length=20)
    speciality = forms.CharField(label='Speciality', max_length=20)
    company = forms.CharField(label = 'Company',max_length=30)
    created_at = forms.DateTimeField('date created')
    updated_at = forms.DateTimeField('date updated')

