"""GroupsApp URL

Created by Naman Patwari on 10/10/2016.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^group/all$', views.getGroups, name='Groups'),
    url(r'^group/form$', views.getGroupForm, name='GroupForm'),
    url(r'^group/formsuccess$', views.getGroupFormSuccess, name='GroupFormSuccess'),
    url(r'^group/join$', views.joinGroup, name='GJoin'),
    url(r'^group/unjoin$', views.unjoinGroup, name='GUnjoin'),
    url(r'^group$', views.getGroup, name='Group'),
    url(r'^group/invitestudent$', views.inviteStudent, name='InviteStudent'),
    url(r'^group/comments', views.getComments, name='GetComments'),
    url(r'^group/delete', views.deleteGroup, name='DeleteGroup'),
    url(r'^group/project', views.chooseProject, name='ChooseProject'),
]
