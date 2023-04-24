from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def index(request, id):
    return HttpResponse(render(request, 'payapp/index.html', {'id': id}))
