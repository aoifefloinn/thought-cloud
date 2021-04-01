from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('This is the diary landing page. It loads the data \
      for a specific diary and displays it (so, the entries).')
