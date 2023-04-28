from django.shortcuts import render

from django.http import HttpResponse


def usd_to_gbp(request, amount):
    return HttpResponse(amount * 0.80)


def gbp_to_dollar(request, amount):
    return HttpResponse(amount * 1.25)

