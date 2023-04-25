import json

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.


def homePage(request):
    return HttpResponse(render(request, 'payapp/homePage.html'))


def loginPage(request):
    return HttpResponse(render(request, 'payapp/loginPage.html'))


def signUp(request):
    return HttpResponse(render(request, 'payapp/signupPage.html'))


def dashboardPage(request):
    return HttpResponse(render(request, 'payapp/dashboardPage.html'))

