from django.http import HttpResponse
from django.shortcuts import render, loader
from .models import Item, Order, OrderItem
from django.contrib.auth.models import User

import os
import json

# Create your views here.
def index(request):

  items = Item.objects.all()
  contexts = {}
  for item in items:
    _id = item.id
    _name = item.name
    _type = item.category
    _image = item.image
    _tag = item.tag
    _price = item.price
    _avail = item.stock


    data = {'id':_id, 'img': _image, 'name':_name, 'tag': _tag, 'price':_price, 'avail': _avail }

    if(contexts.get(_type)):
      contexts[_type].append(data)
    else:
      contexts[_type] = [data]

  contexts['posters'] = []
  for files in os.listdir( os.getcwd() +"/pages/static/pages/image/posters"):
    contexts['posters'].append(files)

  response = render(request, 'pages/index.html', contexts)
  return HttpResponse(response)

def order(request):
  if request.user.is_anonymous:
    return HttpResponse(render(request, 'login/login.html', {"result":""}))
  else:
    context = {}
    response = render(request, 'pages/order.html', context)
    return HttpResponse(response)

def order_done(request):
  body_unicode = request.body.decode('utf-8') 
  body = json.loads(body_unicode)
  items = body['order']

  print(request.user)
  user = User.objects.get(username = request.user)
  order_db = Order()
  order_db.user = user
  order_db.address = body['address']
  order_db.save()
  
  
  for item in items:
    print(item)
    item_db = OrderItem()
    item_db.itemId = item['id']
    item_db.orderId = order_db.id
    item_db.quantity = item['qyt']
    item_db.description = item['des']
    item_db.totalCost = item['price']
    item_db.save()


  return HttpResponse("Working")

