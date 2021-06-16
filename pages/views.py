from django.http import HttpResponse, FileResponse
from django.shortcuts import render, loader
from .models import Item, Order, OrderItem
from django.contrib.auth.models import User

import os
import json
import time
from pages import pdfgen
from reportlab.pdfgen import canvas
import webbrowser, os


class header:
  def __init__(self,CustomerName,CustomerContact, orderId):
    self.InvoiceNumber= orderId
    self.CustomerName=CustomerName
    self.CustomerContact=CustomerContact
    timedate=time.asctime()
    self.date=timedate[4:8]+timedate[8:10]+", "+timedate[20:24]+"."
    self.time=" "+timedate[11:20]
class product:
  def __init__(self,name,quantity,rate,tax,discount):
    self.name=name
    self.quantity=quantity
    self.rate=rate
    self.tax=tax
    self.total=(quantity*rate)-discount
    self.discount=discount


def index(request):

  items = Item.objects.all()
  contexts = {}
  for item in items:
    _id = item.id
    _name = item.name
    _type = item.category
    _image = item.image.url
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
  

  Products = []
  for item in items:
    print(item)
    item_db = OrderItem()
    item_db.itemId = item['id']
    item_db.orderId = order_db.id
    item_db.quantity = item['qyt']
    item_db.description = item['des']
    item_db.totalCost = item['price']
    item_db.save()
    temp = [item['item'], int(item['qyt']), float(item['price'])/float(item['qyt']), 0, float(item['price']), 18.0]
    Products.append(temp)

  genratePDF(request.user, '123456789', order_db.id, Products)

  path = './Invoice/'+str(order_db.id)+'.pdf'
  # with open(path, 'rb') as fh:  
  #   response = HttpResponse(fh.read(), content_type="application/pdf")
  #   response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
  response = FileResponse(open(path, 'rb'))  
  return HttpResponse( response)

  return HttpResponse("Working")

def genratePDF(custName, custCont, orderId, Products ):

  head=header(custName, custCont, orderId)
  pdf= canvas.Canvas(".\\Invoice\\"+str(int(head.InvoiceNumber))+".pdf")
  pdfgen.header(head,pdf)
  pdfgen.middle(pdf)
  ycooridinate=650
  x=1

  for item in Products:
      currproduct=product(item[0],item[1],item[2],item[5],item[3])
      pdf.drawString(35,ycooridinate,str(x))
      x=x+1
      pdf.setFont("Courier-Bold",9)
      ycooridinate=pdfgen.additem(currproduct,pdf,ycooridinate)
      print(item)
  pdf.setFont("Courier-Bold",11)
  pdfgen.footer(pdf,Products)
  pdf.save()
  webbrowser.open(".\\InvoiceGenerator\\"+str(int(head.InvoiceNumber))+".pdf")


