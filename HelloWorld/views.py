

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request) :
    return render(request, 'home.html' , { 'name' : 'Akshara'})

def index(response) :
    return HttpResponse("<h1>Hi 2 time Akshara</h1>")

def neighbor(response) :
    return HttpResponse("<h1> Akshara's Neighbor</h1>")
