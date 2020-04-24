from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def login(request):
    return HttpResponse(" 你好，欢迎访问 login.")

def home(request):
    return HttpResponse(" 你好，欢迎访问 home.")


