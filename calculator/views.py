from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def dashboard(request) :
    return render(request,'dashboard.html' , {'name' : 'Akshara'})

def add(request) :

    # just remember why we changes from GET to POST while giving value to the server
    # Show the calculator form when /add/ is opened without submitted values.
    if 'num1' not in request.POST or 'num2' not in request.POST:
        return render(request, 'add.html')

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    result = val1 + val2

    return render(request, 'result.html' , {'result' : result})
