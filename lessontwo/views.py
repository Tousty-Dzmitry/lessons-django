from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def two(request):
    return HttpResponse("This is lesson two.")