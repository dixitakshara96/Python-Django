from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def dashboard(request) :
    return render(request,'dashboard.html' , {'name' : 'Akshara'})

def add(request) :


    # didn't get the logic  
    # Show the calculator form when /add/ is opened without submitted values.
    if 'num1' not in request.GET or 'num2' not in request.GET:
        return render(request, 'add.html')

    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])

    result = val1 + val2

    return render(request, 'result.html' , {'result' : result})
