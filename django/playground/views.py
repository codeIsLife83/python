from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. AKA request handlers

def say_hello(request):
    x=1
    y=2
    return render(request, "hello.html", {'date': '2021-01-01', "items": ["apple", "banana", "cherry"]})

