from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.utils.crypto import get_random_string

class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control"}))

class AdminRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your username"}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control",  "placeholder": "Create password"}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control",  "placeholder": "Confirm password"}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={"class": "form-control",  "placeholder": "Enter your email"}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={"class": "form-control",  "placeholder": "Enter your phone number"}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control",  "placeholder": "Enter your address"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'password1', 'password2']

class BuyerRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your username"}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control",  "placeholder": "Create password"}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control",  "placeholder": "Confirm password"}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={"class": "form-control",  "placeholder": "Enter your email"}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={"class": "form-control",  "placeholder": "Enter your phone number"}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control",  "placeholder": "Enter your address"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'password1', 'password2']
        
class VendorRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your username"}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control",  "placeholder": "Create password"}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control",  "placeholder": "Confirm password"}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={"class": "form-control",  "placeholder": "Enter your email"}))
    phone = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={"class": "form-control",  "placeholder": "Enter your phone number"}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control",  "placeholder": "Enter your address"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'password1', 'password2']

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your username"}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control",  "placeholder": "Create password"}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control",  "placeholder": "Confirm password"}))
#     email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control",  "placeholder": "Enter your email"}))
#     role = forms.ChoiceField(choices=[('ADMIN', 'Admin'), ('BUYER', 'Buyer'), ('VENDOR', 'Vendor')], widget=forms.RadioSelect(attrs={"class": "form-check-input"}))

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', 'role')
    
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.username = self.cleaned_data['username']
#         user.email = self.cleaned_data['email']
#         role = self.cleaned_data['role']
#         vendorid = get_random_string(length=13)
            
#         if role == 'BUYER':
#             user.is_buyer = True
#             buyer = BuyerProfile.objects.create(user=user, username=user.username, email=user.email)
#             # set additional fields for buyer model here
#         elif role == 'VENDOR':
#             user.is_vendor = True
#             vendor = VendorProfile.objects.create(user=user, username=user.username, email=user.email, vendorid=vendorid)
#             # set additional fields for vendor model here
#         else:
#             user.is_admin = True
#             admin = AdminProfile.objects.create(user=user,  username=user.username, email=user.email)
#             # set additional fields for admin model here
            
#         if commit:
#             user.save()

#         return user