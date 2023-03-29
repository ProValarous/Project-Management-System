from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def create_project(request):
    return render(request,'createproject.html')
