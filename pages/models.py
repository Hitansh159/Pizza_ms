from django.db import models

class Item(models.Model):
  image = models.ImageField()
  category = models.CharField(max_length = 255)
  name = models.CharField(max_length = 255)
  price = models.DecimalField(decimal_places=2, max_digits=5)
  tag = models.TextField()
  stock = models.BooleanField()

class Order(models.Model):
  user = models.OneToOneField('login.Customer', on_delete=models.CASCADE)
  


class OrderItem(models.Model):
  itemId = models.ForeignKey('Item', on_delete=models.CASCADE )
  orderId = models.ForeignKey('Order', on_delete=models.CASCADE)
  quantity = models.IntegerField()
  totalCost = models.DecimalField(decimal_places=2, max_digits=10)



