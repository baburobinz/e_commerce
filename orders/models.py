from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.

class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STAUS_CHOICE = (
        (ORDER_PROCESSED,"Order Processed"),
        (ORDER_DELIVERED,"Order delivered"),
        (ORDER_REJECTED,"Order Rejected")
        )
    order_status = models.IntegerField(choices=STAUS_CHOICE,default=CART_STAGE)
    owner = models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name="orders",null=True)
    total_price = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)

    def total(self):
        cart_items = self.added_items.all()
        total_amt = 0
        for i in cart_items:
            total_amt+=i.sub_total()
        return total_amt
    
    def __str__(self):
        return "order-{}-{}".format(self.id,self.owner.user.username)

class OrderedItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='add_carts',null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')
    def sub_total(self):
        return self.product.price*self.quantity
    def __str__(self):
        return "item-{}".format(self.product.title)
    