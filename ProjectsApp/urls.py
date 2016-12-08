"""ProjectsApp URL Configuration

Created by Harris Christiansen on 10/02/16.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^project/all$', views.getProjects, name='Projects'),
    url(r'^bookmark/all$', views.getBookmarks, name='Bookmarks'),
    url(r'^addbookmark$', views.addBookmark, name='AddBookmark'),
    url(r'^removebookmark$', views.removeBookmark, name='RemoveBookmark'),
    url(r'^removebookmarklist$', views.removeBookmarkList, name='RemoveBookmarkList'),
    # url(r'^project$', views.getProject, name='Project'),
]