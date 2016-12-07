"""AuthenticationApp Views

Created by Naman Patwari on 10/4/2016.
"""

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginForm, RegisterForm, UpdateForm, UniversityForm, CompanyForm
from .models import MyUser, Student, Engineer, Teacher


# Auth Views

def auth_login(request):
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next')
    if next_url is None:
        next_url = "/"
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            messages.success(request, 'Success! Welcome, ' + (user.first_name or ""))
            login(request, user)
            return HttpResponseRedirect(next_url)
        else:
            messages.warning(request, 'Invalid username or password.')

    context = {
        "form": form,
        "page_name": "Login",
        "button_value": "Login",
        "links": ["register"],
    }
    return render(request, 'auth_form.html', context)


def auth_logout(request):
    logout(request)
    messages.success(request, 'Success, you are now logged out')
    return render(request, 'index.html')


def auth_register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        new_user = MyUser.objects.create_user(email=form.cleaned_data['email'],
                                              password=form.cleaned_data["password2"],
                                              first_name=form.cleaned_data['firstname'],
                                              last_name=form.cleaned_data['lastname'],
                                              role=form.cleaned_data["role"],
                                              about=form.cleaned_data['about'],
                                              contact_info=form.cleaned_data['contactinfo'])
        new_user.save()

        login(request, new_user)

        return HttpResponseRedirect(reverse('ChooseRole'))

    context = {
        "form": form,
        "page_name": "Register",
        "button_value": "Register",
        "links": ["login"],
    }
    return render(request, 'auth_form.html', context)


def choose_role(request):
    uni = False
    com = False
    if "Student" or "Teacher" in request.user.role:
        form = UniversityForm(request.POST or None)
        uni = True
        com = False

    if "Engineer" in request.user.role:
        form = CompanyForm(request.POST or None)
        uni = False
        com = True

    # noinspection PyUnboundLocalVariable
    if form.is_valid():
        if uni is True:
            from UniversitiesApp import models
            in_university = models.University.objects.get(name__exact=form.cleaned_data['university'])
            in_university.members.add(request.user)
            in_university.save()
            request.user.university_set.add(in_university)
            request.user.user_university = models.University.objects.get(name__exact=form.cleaned_data['university']).name
            request.user.save()

            if "Student" in request.user.role:
                new_student = Student(user=request.user)
                new_student.save()

            if "Teacher" in request.user.role:
                new_teacher = Teacher(user=request.user)
                new_teacher.save()

            messages.success(request, 'Success! Your account was created and you have chosen a University!')

        if com is True:
            from CompaniesApp import models
            in_company = models.Company.objects.get(name__exact=form.cleaned_data['company'])
            in_company.members.add(request.user)
            in_company.save()
            request.user.company_set.add(in_company)
            request.user.user_company = models.Company.objects.get(name__exact=form.cleaned_data['company']).name
            request.user.save()

            new_engineer = Engineer(user=request.user)
            new_engineer.save()

            messages.success(request, 'Success! Your account was created and you have chosen a Company!')

        return render(request, 'index.html')

    context = {
        "form": form,
        "page_name": "Choose",
        "button_value": "Choose",
        "links": ["login"],
    }

    return render(request, 'auth_form.html', context)


@login_required
def update_profile(request):
    form = UpdateForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Success, your profile was saved!')

    context = {
        "form": form,
        "page_name": "Update",
        "button_value": "Update",
        "links": ["logout"],
    }
    return render(request, 'auth_form.html', context)
