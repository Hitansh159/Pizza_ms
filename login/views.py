from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# include "pages/order.html" 

def signup(request):
	return HttpResponse(render(request, 'login/signup.html', {}))

def signup_test(request):

	user = User.objects.create_user(request.POST['name'], password= request.POST['password'])
	user.email = request.POST['id'];

	user.save()

	return redirect("/auth/")

def login_pag(request):
  return HttpResponse(render(request, 'login/login.html', {"result":""}))

def login_test(request):
	user = authenticate(request = request, email= request.POST['id'], password=request.POST['password'])

	if user is not None:
		login(request, user)
		return redirect("/order")
	else:
		return HttpResponse(render(request, 'login/login.html', {"result":"Incorrect Username or password"}))

def signout(request):
	logout(request)
	return redirect('/')