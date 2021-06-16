from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Customer
# include "pages/order.html" 

def login_pag(request):
  return HttpResponse(render(request, 'login/login.html', {"result":""}))

def login_test(request):
	print(request.POST)
	user = authenticate(request = request, username= request.POST['id'], password=request.POST['password'])

	if user is not None:
		login(request, user)
		return HttpResponse(render(request, 'pages/order.html', {}))
	else:
		return HttpResponse(render(request, 'login/login.html', {"result":"Incorrect Username or password"}))

def signup(request):
	return HttpResponse(render(request, 'login/signup.html', {}))

def signup_test(request):

	user = User.objects.create_user(request.POST['id'], password= request.POST['password'])
	user.save()

	return HttpResponse(render(request, 'login/login.html', {}))