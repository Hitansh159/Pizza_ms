from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="Home Page"),
  path('order/', views.order, name="Order"),
  path('order_done/', views.order_done, name="order done"),
  path('acknowledgement/', views.acknowledgement, name="acknowledgement"),
  path('my_orders/', views.my_order, name="my orders"),
  path('payment/', views.payment, name="payment"),
  path('paypal/', views.paypal, name="paypal"),
  path('netbanking/', views.netbanking, name="netbanking")
]