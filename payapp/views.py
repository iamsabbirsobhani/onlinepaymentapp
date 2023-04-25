import json

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.


def index(request):
    return HttpResponse(render(request, 'payapp/homePage.html'))
