from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("This is the response")

def home(request):
    context = {"name" : " Junior"}
    return render(request, "vetoffice/home.html", context)