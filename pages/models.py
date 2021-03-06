from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
  image = models.ImageField()
  category = models.CharField(max_length = 255)
  name = models.CharField(max_length = 255)
  price = models.DecimalField(decimal_places=2, max_digits=5)
  tag = models.TextField()
  stock = models.BooleanField()

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  address = models.TextField(default = "")
  date = models.DateTimeField(auto_now=True)
  bill = models.FileField(upload_to ="invoice/", default='invoice/default.pdf' )


class OrderItem(models.Model):
  itemId = models.IntegerField()
  orderId = models.IntegerField()
  quantity = models.IntegerField()
  description = models.TextField(default = "")
  totalCost = models.DecimalField(decimal_places=2, max_digits=10)

  status_choice = [
    ('order' , 'ordered'),
    ('cancel', 'canceled')
  ]

  status = models.CharField(max_length=6, choices=status_choice, default = 'order')



