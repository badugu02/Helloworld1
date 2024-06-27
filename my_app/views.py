from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greet(request):
    return HttpResponse("hello world")

def product(request):
    return HttpResponse("product")