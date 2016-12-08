from django.shortcuts import render

from GroupsApp.models import Group
from . import forms
from . import models


# noinspection PyPep8Naming
# Create your views here.
def getComments(request):
    in_group_name = request.GET.get('name', 'None')
    in_group = models.Group.objects.get(name__exact=in_group_name)
    is_member = in_group.members.filter(email__exact=request.user.email)
    comments_list = models.Comment.objects.all()
    context = {
        'user': request.user,
        'comments': comments_list,
        'userIsMember': is_member,
        'group': in_group
    }
    return render(request, 'comments.html', context)


# noinspection PyPep8Naming
def getCommentForm(request):
    if request.user.is_authenticated:
        in_name = request.GET.get('name', 'None')
        in_group = models.Group.objects.get(name__exact=in_name)
        is_member = in_group.members.filter(email__exact=request.user.email)
        context = {
            'user': request.user,
            'group': in_group,
            'userIsMember': is_member,
        }
        return render(request, 'commentForm.html', context)
    return render(request, 'autherror.html')


# noinspection PyPep8Naming
def addComment(request):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST or None)
        if form.is_valid():
            in_name = request.GET.get('name', 'None')
            in_group = Group.objects.get(name__exact=in_name)
            is_member = in_group.members.filter(email__exact=request.user.email).exists()
            new_comment = models.Comment(comment=form.cleaned_data['comment'])
            new_comment.group = in_group
            new_comment.comment_by = request.user
            new_comment.save()
            comments_list = models.Comment.objects.all()
            context = {
                'user': request.user,
                'comments': comments_list,
                'group': in_group,
                'userIsMember': is_member,
            }
            return render(request, 'comments.html', context)
            # return HttpResponseRedirect(reverse('Comments'))
        else:
            form = forms.CommentForm()
    return render(request, 'comments.html')


# noinspection PyPep8Naming
def deleteComment(request):
    if request.user.is_authenticated:
        in_name = request.GET.get('name', 'None')
        in_group = Group.objects.get(name__exact=in_name)
        is_member = in_group.members.filter(email__exact=request.user.email)
        in_comment_desc = request.GET.get('comment', 'None')
        in_comment = request.user.comment_set.get(comment=in_comment_desc)
        in_comment.delete()
        comments_list = models.Comment.objects.all()
        context = {
            'user': request.user,
            'comments': comments_list,
            'group': in_group,
            'userIsMember': is_member,
        }
        return render(request, 'comments.html', context)

    return render(request, 'autherror.html')
