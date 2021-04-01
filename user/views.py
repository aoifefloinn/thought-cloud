from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('This is the user dashboard. It will display \
      user info and diaries written (or it will redirect to the login page).')
