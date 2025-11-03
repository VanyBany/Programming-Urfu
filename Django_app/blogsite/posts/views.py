from django.shortcuts import render
from django.http import HttpResponse
def check_connection(request):
    return HttpResponse("all good man")


# Create your views here.

