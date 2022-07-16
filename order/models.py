from django.db import models
from shop.models import Product

class Order(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    jrnl_no = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
class account_number(models.Model):
    bob=models.CharField(max_length=200, blank=True)
    bnb=models.CharField(max_length=200, blank=True)
    pnb=models.CharField(max_length=200, blank=True)
    bdb=models.CharField(max_length=200, blank=True)


class inventory(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True,)
    def __str__(self):
     return f"{self.created.strftime('%d-%m-%Y')}"