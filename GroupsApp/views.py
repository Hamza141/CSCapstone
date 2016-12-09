"""GroupsApp Views
Created by Naman Patwari on 10/10/2016.
"""
from django.shortcuts import render

from CommentsApp.models import Comment
from . import forms
from . import models
from .models import MyUser


# noinspection PyPep8Naming
def getGroups(request):
    if request.user.is_authenticated():
        groups_list = models.Group.objects.all()
        context = {
            'groups': groups_list,
        }
        return render(request, 'groups.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def getGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        is_member = in_group.members.filter(email__exact=request.user.email).exists()
        context = {
            'group': in_group,
            'userIsMember': is_member,
        }
        return render(request, 'group.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def getGroupForm(request):
    if request.user.is_authenticated():
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def getGroupFormSuccess(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.GroupForm(request.POST)
            if form.is_valid():
                if models.Group.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    return render(request, 'groupform.html', {'error': 'Error: That Group name already exists!'})
                new_group = models.Group(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
                new_group.save()
                context = {
                    'name': form.cleaned_data['name'],
                }
                return render(request, 'groupformsuccess.html', context)
        else:
            form = forms.GroupForm()
        return render(request, 'groupform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def joinGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_group.members.add(request.user)
        in_group.save()
        request.user.group_set.add(in_group)
        request.user.save()
        context = {
            'group': in_group,
            'userIsMember': True,
        }
        return render(request, 'group.html', context)
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def unjoinGroup(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        in_group.members.remove(request.user)
        in_group.save()
        request.user.group_set.remove(in_group)
        request.user.save()
        context = {
            'group': in_group,
            'userIsMember': False,
        }
        return render(request, 'group.html', context)
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def inviteStudent(request):
    form = forms.InvitationForm(request.POST)
    if request.user.is_authenticated():
        if form.is_valid():
            student = MyUser.objects.get_by_natural_key(form.cleaned_data['student'])

            in_name = request.GET.get('name', 'None')
            in_group = models.Group.objects.get(name__exact=in_name)
            in_group.members.add(student)
            in_group.save()
            student.group_set.add(in_group)
            student.save()
            context = {
                'group': in_group,
                'userIsMember': True,
            }

            return render(request, 'group.html', context)

        context = {
            "form": form,
            "page_name": "Invite Student",
            "button_value": "Invite",
            "links": ["logout"],
        }

        return render(request, 'invitationform.html', context)
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def getComments(request):
    if request.user.is_authenticated:
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        is_member = in_group.members.filter(email__exact=request.user.email).exists()
        comments_list = Comment.objects.all()
        context = {
            'user': request.user,
            'group': in_group,
            'userIsMember': is_member,
            'comments': comments_list,
        }
        return render(request, 'comments.html', context)

    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def deleteGroup(request):
    if request.user.is_authenticated:
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        # from ProjectsApp.models import Project
        # project = Project.objects.get(assigned_to=in_group)
        # in_group.project_set.remove(in_group)
        in_group.delete()
        groups_list = models.Group.objects.all()
        context = {
            'groups': groups_list,
        }
        return render(request, 'groups.html', context)

    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def getProjects(request):
    if request.user.is_authenticated:
        from . import models
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        # in_group.delete()
        # groups_list = models.Group.objects.all()
        from ProjectsApp import models
        projects_list = models.Project.objects.all()
        des = in_group.description.split()
        count = des.__len__()

        # from AuthenticationApp.models import MyUser
        # members = MyUser.groups_set

        des2 = request.user.about.split()
        count2 = des2.__len__()
        from ProjectsApp.models import Project
        x = Project
        for x in projects_list:
            x.show = False
        for x in projects_list:
            for i in range(0, count):
                if des.__getitem__(i) in x.programmingLanguage:
                    x.show = True
                    break
                if des.__getitem__(i) in x.speciality:
                    x.show = True
                    break
                if des.__getitem__(i) is x.description:
                    x.show = True
                    break
            for i in range(0, count2):
                if des2.__getitem__(i) in x.programmingLanguage:
                    x.show = True
                    break
                if des2.__getitem__(i) in x.speciality:
                    x.show = True
                    break
                if des2.__getitem__(i) is x.description:
                    x.show = True
                    break

        context = {
            'projects': projects_list,
            'group': in_group,
        }
        return render(request, 'projects.html', context)

    return render(request, 'autherror.html')
