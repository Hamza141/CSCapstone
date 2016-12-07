"""
UniversitiesApp Views

Created by Jacob Dunbar on 11/5/2016.
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import forms
from . import models
from .models import MyUser


# noinspection PyPep8Naming
def getUniversities(request):
    if request.user.is_authenticated():
        universities_list = models.University.objects.all()
        context = {
            'universities': universities_list,
        }
        return render(request, 'universities.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def getUniversity(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_name)
        is_member = in_university.members.filter(email__exact=request.user.email)
        context = {
            'university': in_university,
            'userIsMember': is_member,
        }
        return render(request, 'university.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def getUniversityForm(request):
    if request.user.is_authenticated():
        return render(request, 'universityform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')


# noinspection PyPep8Naming,SpellCheckingInspection
def getUniversityFormSuccess(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.UniversityForm(request.POST, request.FILES)
            if form.is_valid():
                if models.University.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    return render(request, 'universityform.html',
                                  {'error': 'Error: That university name already exists!'})
                new_university = models.University(name=form.cleaned_data['name'],
                                                   photo=request.FILES['photo'],
                                                   description=form.cleaned_data['description'],
                                                   website=form.cleaned_data['website'])
                new_university.save()
                context = {
                    'name': form.cleaned_data['name'],
                }
                return render(request, 'universityformsuccess.html', context)
            else:
                return render(request, 'universityform.html', {'error': 'Error: Photo upload failed!'})
        else:
            form = forms.UniversityForm()
        return render(request, 'universityform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def joinUniversity(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_name)
        in_university.members.add(request.user)
        in_university.save()
        request.user.user_university = in_university.name
        request.user.university_set.add(in_university)
        request.user.save()
        context = {
            'university': in_university,
            'userIsMember': True,
        }
        return render(request, 'university.html', context)
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def unjoinUniversity(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_name)
        in_university.members.remove(request.user)
        in_university.save()
        request.user.user_university = None
        request.user.university_set.remove(in_university)
        request.user.save()
        context = {
            'university': in_university,
            'userIsMember': False,
        }
        return render(request, 'university.html', context)
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def getCourse(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_course_tag = request.GET.get('course', 'None')
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        is_member = in_course.members.filter(email__exact=request.user.email)
        userIsMember = in_university.members.filter(email__exact=request.user.email)
        context = {
            'university': in_university,
            'course': in_course,
            'userInCourse': is_member,
            'userIsMember': userIsMember,
        }
        return render(request, 'course.html', context)
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def courseForm(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        context = {
            'university': in_university,
        }
        return render(request, 'courseform.html', context)
        # render error page if user is not logged in
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def addCourse(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.CourseForm(request.POST)
            if form.is_valid():
                in_university_name = request.GET.get('name', 'None')
                in_university = models.University.objects.get(name__exact=in_university_name)
                if in_university.course_set.filter(tag__exact=form.cleaned_data['tag']).exists():
                    return render(request, 'courseform.html',
                                  {'error': 'Error: That course tag already exists at this university!'})
                new_course = models.Course(tag=form.cleaned_data['tag'],
                                           name=form.cleaned_data['name'],
                                           description=form.cleaned_data['description'],
                                           university=in_university)
                new_course.save()
                in_university.course_set.add(new_course)
                is_member = in_university.members.filter(email__exact=request.user.email)
                context = {
                    'university': in_university,
                    'userIsMember': is_member,
                }
                return render(request, 'university.html', context)
            else:
                return render(request, 'courseform.html', {'error': 'Undefined Error!'})
        else:
            form = forms.CourseForm()
            return render(request, 'courseform.html')
            # render error page if user is not logged in
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def removeCourse(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_course_tag = request.GET.get('course', 'None')
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        in_course.delete()
        is_member = in_university.members.filter(email__exact=request.user.email)
        context = {
            'university': in_university,
            'userIsMember': is_member,
        }
        return render(request, 'university.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def joinCourse(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_course_tag = request.GET.get('course', 'None')
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        in_course.members.add(request.user)
        in_course.save()
        request.user.course_set.add(in_course)
        request.user.save()
        userIsMember = in_university.members.filter(email__exact=request.user.email)

        context = {
            'university': in_university,
            'course': in_course,
            'userInCourse': True,
            'userIsMember': userIsMember,
        }
        return render(request, 'course.html', context)
    return render(request, 'autherror.html')


# noinspection PyPep8Naming,SpellCheckingInspection
def unjoinCourse(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_course_tag = request.GET.get('course', 'None')
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        in_course.members.remove(request.user)
        in_course.save()
        request.user.course_set.remove(in_course)
        request.user.save()
        userIsMember = in_university.members.filter(email__exact=request.user.email)

        context = {
            'university': in_university,
            'course': in_course,
            'userInCourse': False,
            'userIsMember': userIsMember,
        }
        return render(request, 'course.html', context)
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def addStudent(request):
    form = forms.AddStudentForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            student = MyUser.objects.get_by_natural_key(form.cleaned_data['student'])

            in_university_name = request.GET.get('name', 'None')
            in_university = models.University.objects.get(name__exact=in_university_name)
            in_course_tag = request.GET.get('course', 'None')
            in_course = in_university.course_set.get(tag__exact=in_course_tag)
            in_course.members.add(student)
            in_course.save()
            student.course_set.add(in_course)
            student.save()
            userIsMember = in_university.members.filter(email__exact=request.user.email)

            context = {
                'university': in_university,
                'course': in_course,
                'userInCourse': True,
                'userIsMember': userIsMember,
            }
            return render(request, 'course.html', context)
            #return HttpResponseRedirect(reverse('Course'))

        context = {
            "form": form,
            "page_name": "Add Student",
            "button_value": "Add",
            "links": ["logout"],
        }

        return render(request, 'addstudentform.html', context)

    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def removeStudent(request):
    if request.user.is_authenticated():
        in_user_name = request.GET.get('email', 'None')
        in_user = MyUser.objects.get_by_natural_key(in_user_name)
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_course_tag = request.GET.get('course', 'None')
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        in_course.members.remove(in_user)
        in_course.save()
        in_user.course_set.remove(in_course)
        in_user.save()
        userIsMember = in_university.members.filter(email__exact=request.user.email)

        context = {
            'university': in_university,
            'course': in_course,
            'userInCourse': True,
            'userIsMember': userIsMember,
        }
        return render(request, 'course.html', context)
    return render(request, 'autherror.html')
