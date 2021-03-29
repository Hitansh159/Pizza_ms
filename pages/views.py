from django.http import HttpResponse
from django.shortcuts import render, loader

import os
import json

# Create your views here.
def index(request):
  context = {}
  paths = [
    'pizzas',
    'breads',
    'posters',
    'drinks_desserts',
    'combos'
  ] 
  for folder in paths:
    for files in os.listdir( os.getcwd() +"/pages/static/pages/image/" + folder ):
      if(context.get(folder)):
        context[folder].append({'img': files, 'details': files})
      else:
        context[folder] = [{'img': files, 'details': files}]
        
  response = render(request, 'pages/index.html', context)
  return HttpResponse(response)

def order(request):

  # return HttpResponse(str(request.user))

  if not request.user.is_anonymous:
  # context = {'order': [{'id': 25, 'name': 'pizza', 'cost': 50 }]}
    context = {}
    response = render(request, 'pages/order.html', context)
    return HttpResponse(response)

  else:
    return HttpResponse('working!')
