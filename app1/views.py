from django.shortcuts import render
from django.http import HttpResponse
def string1(request):
    return HttpResponse('This is the first View of string1')
def string2(request):
    return HttpResponse('This is the second View of string2')


# Create your views here.
