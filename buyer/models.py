from django.db import models
from customadmin.models import *
from vendor.models import Product
from djmoney.models.fields import MoneyField, Money
from django.conf import settings

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(BuyerProfile, on_delete=models.CASCADE)
    # products = models.ForeignKey(Product, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    subtotal = MoneyField(max_digits=14, decimal_places=2, default_currency='INR', default=Money(0, 'INR'))
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.products} x {self.quantity} in {self.id}"

    # def update_subtotal(self):
    #     total = Money(0, 'INR')
    #     for cart_product in self.cartproduct_set.all():
    #         total += cart_product.product.price * cart_product.quantity
    #     self.subtotal = total
    #     self.save()
        
class Order(models.Model):
    user = models.ForeignKey(BuyerProfile, on_delete=models.CASCADE, related_name='orders')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField('Phone', null=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s order on {self.ordered_at}"    