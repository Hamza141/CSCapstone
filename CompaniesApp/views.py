"""
CompaniesApp Views

Created by Jacob Dunbar on 10/2/2016.
"""
import datetime

from django.shortcuts import render

from CompaniesApp.forms import ProjectForm
from ProjectsApp.models import Project
from . import forms
from . import models


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
        form = ProjectForm(request.POST or None)

        if form.is_valid():
            in_name = request.GET.get('name', 'None')
            in_company = models.Company.objects.get(name__exact=in_name)
            is_member = in_company.members.filter(email__exact=request.user.email)

            new_project = Project(name=form.cleaned_data['name'],
                                  description=form.cleaned_data["description"],
                                  yearsOfExperience=form.cleaned_data['yearsOfExperience'],
                                  programmingLanguage=form.cleaned_data['programmingLanguage'],
                                  speciality=form.cleaned_data["speciality"],
                                  )
            # contact_info=form.cleaned_data['contactinfo'])
            new_project.company = in_company
            new_project.created_at = datetime.datetime.now()
            new_project.save()
            in_company.project_set.add(new_project)
            context = {
                'company': in_company,
                'userIsMember': is_member,
            }
            return render(request, 'company.html', context)

        context = {
            "form": form,
            "page_name": "Add a Project",
            "button_value": "Add",
            "links": ["logout"],
        }
        return render(request, 'projectform.html', context)

    return render(request, "autherror.html")

    """"" if request.user.is_authenticated():
            if request.method == 'POST':
                form = forms.ProjectForm(request.POST or None)
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
                                                 assignedTo=form.cleaned_data['assignedTo'],
                                                 yearsOfExperience=form.cleaned_data['yearsOfExperience'],
                                                 programmingLanguage=form.cleaned_data['programmingLanguage'],
                                                 speciality=form.cleaned_data['speciality'],
                                                 company=in_company_name)
                    from . import models
                    new_project.save()
                    in_company.project_set.add(new_project)
                    is_member = in_company.members.filter(email__exact=request.user.email)
                    context = {
                        'company': in_company,
                        'userIsMember': is_member,
                    }
                    return render(request, 'company.html', context)

                context = {
                    "form": form,
                    "page_name": "Add Project",
                    "button_value": "Add",
                    "links": ["logout"],
                }
                return render(request, 'projectform.html', context)

            else:
                form = forms.ProjectForm()
                context = {
                    "form": form,
                    "page_name": "Add Project",
                    "button_value": "Add",
                    "links": ["logout"],
                }
                return render(request, 'projectform.html', context)
                # render error page if user is not logged in
        return render(request, 'autherror.html')
    """


def getProject(request):
    if request.user.is_authenticated():
        in_company_name = request.GET.get('name', 'None')
        in_company = models.Company.objects.get(name__exact=in_company_name)
        in_project_name = request.GET.get('project', 'None')
        in_project = in_company.project_set.get(name__exact=in_project_name)
        # is_member = in_project.members.filter(email__exact=request.user.email)
        userIsMember = in_company.members.filter(email__exact=request.user.email)
        context = {
            'project': in_project,
            # 'userInProject': is_member,
            'userIsMember': userIsMember,
        }
        return render(request, 'project.html', context)
    return render(request, 'autherror.html')
