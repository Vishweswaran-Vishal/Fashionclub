from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_buyer = models.BooleanField('Is buyer', default=False)
    is_vendor = models.BooleanField('Is vendor', default=False)
    
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    username = models.CharField('Name', max_length=150, blank=True)
    email = models.EmailField('Email', max_length=150, blank=True)
    phone = models.IntegerField('Phone', blank=True)
    address = models.TextField('Address', max_length=150, blank=True)
    
class BuyerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer_profile')
    username = models.CharField('Name', max_length=150, blank=True)
    email = models.EmailField('Email', max_length=150, blank=True)
    phone = models.IntegerField('Phone', blank=True, null=True)
    address = models.TextField('Address', max_length=150, blank=True)
    
class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor_profile')
    username = models.CharField('Name', max_length=150, blank=True)
    email = models.EmailField('Email', max_length=150, blank=True)
    phone = models.IntegerField('Phone', blank=True)
    address = models.TextField('Address', max_length=150, blank=True)
    vendorid = models.CharField('VendorId', max_length=150, blank=True)
    is_verified = models.BooleanField('Is Verified', default=False)
    is_locked = models.BooleanField('Is Locked', default=False)
    
    @classmethod
    def get_total_vendors(cls):
        return cls.objects.count()