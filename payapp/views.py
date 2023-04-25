import json

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.


def index(request, id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}")
    return HttpResponse(render(request, 'payapp/index.html', {'res': json.loads(response.content)}))
