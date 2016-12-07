"""
CompaniesApp Views

Created by Jacob Dunbar on 10/2/2016.
"""
from django.shortcuts import render

from . import models
from . import forms


def getCompanies(request):
    if request.user.is_authenticated():
        companies_list = models.Company.objects.all()
        context = {
            'companies': companies_list,
        }
        return render(request, 'companies.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')


def getCompany(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        is_member = in_company.members.filter(email__exact=request.user.email)
        context = {
            'company': in_company,
            'userIsMember': is_member,
        }
        return render(request, 'company.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')


def getCompanyForm(request):
    if request.user.is_authenticated():
        return render(request, 'companyform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')


def getCompanyFormSuccess(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.CompanyForm(request.POST, request.FILES)
            if form.is_valid():
                if models.Company.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    return render(request, 'companyform.html', {'error': 'Error: That company name already exists!'})
                new_company = models.Company(name=form.cleaned_data['name'],
                                             photo=request.FILES['photo'],
                                             description=form.cleaned_data['description'],
                                             website=form.cleaned_data['website'])
                new_company.save()
                context = {
                    'name': form.cleaned_data['name'],
                }
                return render(request, 'companyformsuccess.html', context)
            else:
                return render(request, 'companyform.html', {'error': 'Error: Photo upload failed!'})
        else:
            form = forms.CompanyForm()
        return render(request, 'companyform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')


def joinCompany(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        in_company.members.add(request.user)
        in_company.save()
        request.user.user_company = in_company.name
        request.user.company_set.add(in_company)
        request.user.save()
        context = {
            'company': in_company,
            'userIsMember': True,
        }
        return render(request, 'company.html', context)
    return render(request, 'autherror.html')


def unjoinCompany(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_name)
        in_company.members.remove(request.user)
        in_company.save()
        request.user.user_company = None
        request.user.company_set.remove(in_company)
        request.user.save()
        context = {
            'company': in_company,
            'userIsMember': False,
        }
        return render(request, 'company.html', context)
    return render(request, 'autherror.html')


def addProject(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.ProjectForm(request.POST)
            if form.is_valid():
                in_company_name = request.GET.get('name', 'None')
                from . import models
                in_company = models.Company.objects.get(name__exact=in_company_name)
                if in_company.course_set.filter(description_exaction=form.cleaned_data['description']).exists():
                    return render(request, 'projectform.html',
                                  {'error': 'Error: That project name already exists at this Company!'})
                from ProjectsApp import models
                new_project = models.Project(name=form.cleaned_data['name'],
                                             description=form.cleaned_data['description'],
                                             yearsOfExperience=form.cleaned_data['yearsOfExperience'],
                                             programmingLanguage=form.cleaned_data['programmingLanguage'],
                                             speciality=form.cleaned_data['speciality'],
                                             company=in_company)
                from . import models
                new_project.save()
                in_company.course_set.add(new_project)
                is_member = in_company.members.filter(email__exact=request.user.email)
                context = {
                    'company': in_company,
                    'userIsMember': is_member,
                }
                return render(request, 'company.html', context)
            else:
                return render(request, 'projectform.html', {'error': 'Undefined Error!'})
        else:
            form = forms.ProjectForm()
            return render(request, 'projectform.html')
            # render error page if user is not logged in
    return render(request, 'autherror.html')
