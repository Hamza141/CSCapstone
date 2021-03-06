"""GroupsApp Forms

Created by Naman Patwari on 10/10/2016.
"""
from django import forms

class GroupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    description = forms.CharField(label='Description', max_length=300)

class InvitationForm(forms.Form):
    from AuthenticationApp import models
    student = forms.ModelChoiceField(queryset=models.Student.objects.all(),required=True)
