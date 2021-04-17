from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="Home Page"),
  path('order/', views.order, name="Order"),
  path('order_done/', views.order_done, name="Order Done")
]