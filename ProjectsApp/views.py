"""ProjectsApp Views

Created by Harris Christiansen on 10/02/16.
"""
from django.shortcuts import render

from . import models


# noinspection PyPep8Naming
def getProjects(request):
    projects_list = models.Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects_list,
    })


# noinspection PyPep8Naming
def getProject(request):
    return render(request, 'project.html')


# noinspection PyPep8Naming
def getBookmarks(request):
    if request.user.is_authenticated():
        bookmarks = models.Bookmark.objects.all()
        context = {
            'bookmarks': bookmarks,
            'user': request.user,
        }
        return render(request, 'bookmarks.html', context)
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def addBookmark(request):
    if request.user.is_authenticated():
        in_company_name = request.GET.get('companyname', 'None')
        in_company = models.Company.objects.get(name__exact=in_company_name)
        in_project_name = request.GET.get('projectname', 'None')
        in_project = models.Project.objects.get(name__exact=in_project_name)
        userIsMember = in_company.members.filter(email__exact=request.user.email).exists()

        new_bookmark = models.Bookmark()
        new_bookmark.userID = request.user
        new_bookmark.projectID = in_project
        new_bookmark.companyID = in_company
        new_bookmark.name = in_company.name + in_project.name + request.user.email
        new_bookmark.save()

        request.user.bookmark_set.add(new_bookmark)
        in_company.bookmark_set.add(new_bookmark)
        in_project.bookmark_set.add(new_bookmark)

        context = {
            'project': in_project,
            'company': in_company,
            'bookmark': new_bookmark,
            'user': request.user,
            'userIsMember': userIsMember,
        }
        return render(request, 'project.html', context)
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def removeBookmark(request):
    if request.user.is_authenticated():
        in_company_name = request.GET.get('companyname', 'None')
        in_company = models.Company.objects.get(name__exact=in_company_name)
        in_bookmark_name = request.GET.get('bookmarkname', 'None')
        in_project_name = request.GET.get('projectname', 'None')
        in_project = models.Project.objects.get(name__exact=in_project_name)
        in_bookmark = in_company.bookmark_set.get(name=in_bookmark_name)
        in_bookmark.delete()
        userIsMember = in_company.members.filter(email__exact=request.user.email).exists()

        context = {
            'project': in_project,
            'company': in_company,
            'bookmark': False,
            'user': request.user,
            'userIsMember': userIsMember,
        }
        return render(request, 'project.html', context)
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def removeBookmarkList(request):
    if request.user.is_authenticated():
        in_company_name = request.GET.get('companyname', 'None')
        in_company = models.Company.objects.get(name__exact=in_company_name)
        in_bookmark_name = request.GET.get('bookmarkname', 'None')
        in_project_name = request.GET.get('projectname', 'None')
        in_project = models.Project.objects.get(name__exact=in_project_name)
        in_bookmark = in_project.bookmark_set.get(name=in_bookmark_name)
        in_bookmark.delete()

        bookmarks = models.Bookmark.objects.all()
        context = {
            'bookmarks': bookmarks,
            'user': request.user,
        }
        return render(request, 'bookmarks.html', context)
    return render(request, 'autherror.html')
