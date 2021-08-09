from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# This is to test the git learning 

def index(request):
    return HttpResponse("Hello, world. This is my test page from testapp1!!! - version 2")
