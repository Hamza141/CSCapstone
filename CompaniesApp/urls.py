"""CompaniesApp URL Configuration

Created by Jacob Dunbar on 10/2/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^company/all$', views.getCompanies, name='Companies'),
	url(r'^company/form$', views.getCompanyForm, name='CompanyForm'),
    url(r'^company/formsuccess$', views.getCompanyFormSuccess, name='CompanyFormSuccess'),
    url(r'^company/join$', views.joinCompany, name='JoinCompany'),
    url(r'^company/unjoin$', views.unjoinCompany, name='UnjoinCompany'),
    url(r'^company$', views.getCompany, name='Company'),
    url(r'^company/project/form$', views.addProject, name="AddProject"),
    url(r'^company/project$', views.getProject, name="Project"),
    url(r'^company/project/remove$', views.removeProject, name="RemoveProject"),
    url(r'^company/project/update$', views.update_profile, name='UpdateProfile'),

]