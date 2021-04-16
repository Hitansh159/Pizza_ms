from django.urls import path
from . import views

urlpatterns = [
  path('', views.login, name='login'),
  path('signup', views.signup, name='signup'),
  path('login_test', views.login_test, name="login_test"),
  path('signup_test', views.signup_test, name="signup_test")  
]