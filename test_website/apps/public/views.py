# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')