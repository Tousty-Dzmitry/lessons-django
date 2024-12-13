from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def three(request):
    return HttpResponse("This is lesson three.")