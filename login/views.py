from django.shortcuts import render
from django.http import HttpResponse

def login(request):
  # template = loader.get_template('login/login.html')
  return HttpResponse(render(request, 'login/login.html'))
