from django.shortcuts import render

from . import models
# Create your views here.
def getComments(request):
    return render(request, 'comments.html')
