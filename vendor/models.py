from django.db import models
from customadmin.models import VendorProfile
from decimal import Decimal
# from buyer.models import *

# Create your models here.

class Product(models.Model):
    vendor = models.ForeignKey(VendorProfile, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    vendor_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    admin_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    gst = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        ordering = ('-created',)
        # index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Calculate the admin profit and gst
        self.admin_profit = Decimal('0.12') * self.vendor_price
        self.gst = Decimal('0.05') * self.vendor_price
        # Calculate the total price
        self.total_price = self.vendor_price + self.admin_profit + self.gst
        super(Product, self).save(*args, **kwargs)