"""GroupsApp Views
Created by Naman Patwari on 10/10/2016.
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import forms
from . import models
from .models import MyUser
from CommentsApp.models import Comment


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
        in_group.save();
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
