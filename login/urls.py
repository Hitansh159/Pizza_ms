from django.urls import path
from . import views

urlpatterns = [
  path('', views.login_pag, name='login'),
  path('signup', views.signup, name='signup'),
  path('login_test', views.login_test, name="login_test"),
  path('signup_test', views.signup_test, name="signup_test"),
  path('signout', views.signout, name="signout")  
]