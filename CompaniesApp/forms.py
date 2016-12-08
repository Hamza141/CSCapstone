"""
CompaniesApp Forms

Created by Jacob Dunbar on 10/3/2016.
"""
from django import forms

from ProjectsApp.models import Project


class CompanyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    photo = forms.ImageField(label='Photo');
    description = forms.CharField(label='Description', max_length=300)
    website = forms.CharField(label='Website', max_length=300)


class ProjectForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    description = forms.CharField(label='Description', max_length=300)
    # assignedTo = forms.CharField(label='Assigned To', max_length=100)
    yearsOfExperience = forms.IntegerField(label="Years of Experience")
    programmingLanguage = forms.CharField(label='Programming Language', max_length=20)
    speciality = forms.CharField(label='Speciality', max_length=20)
    # createdBy = forms.CharField(label="Created By", max_length=50)
    # created_at = forms.DateTimeField('date created')
    # updated_at = forms.DateTimeField('date updated')


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'programmingLanguage', 'yearsOfExperience')
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['programmingLanguage'].label = "Programming Language"
        self.fields['yearsOfExperience'].label = "Years of Experience"

   # def clean_name(self):
    #    return self.initial["name"]
    #def clean_description(self):
       # return self.initial["description"]
    #def programming_language(self):
      #  return self.initial["Programming Language"]
    #def years_of_experience(self):
     #   return self.initial["Years of Experience"]
