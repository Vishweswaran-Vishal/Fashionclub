from django import forms
from .models import Product
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs= {"class": "form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs= {"class": "form-control"}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"class": "form-control-file"}))
    vendor_price = forms.DecimalField(max_digits=10, decimal_places=2, label='Vendor Price', widget=forms.NumberInput(attrs={'id': 'id_vendor_price'}))
    # admin_profit = forms.CharField(widget=forms.TextInput(attrs={'readonly':'18%', 'id': 'admin_profit'}))
    # gst = forms.CharField(widget=forms.TextInput(attrs={'readonly':'5%', 'id': 'gst'}))
    # slug = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'vendor_price')
        