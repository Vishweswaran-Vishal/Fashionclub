from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import *
from buyer.models import *
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return redirect('buyer:home')

def admin_register(request):
    msg = None
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = True
            user.save()
            msg = 'user created'
            admin_profile = AdminProfile.objects.create(
                user = user,
                email = form.cleaned_data['email'],
                username = form.cleaned_data['username'],
                phone = form.cleaned_data['phone'],
                address = form.cleaned_data['address']
            )
            return redirect('customadmin:login_view')
        else:
            msg = 'form is not valid'
    else:
        form = AdminRegistrationForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def buyer_register(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already registered.')
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'This username is already taken.')
            if form.errors:
                # Form is not valid, display error message
                messages.error(request, 'Please correct the errors below.')
            else:
                user = form.save(commit=False)
                user.is_buyer = True
                user.save()
                msg = 'user created'
                buyer_profile = BuyerProfile.objects.create(
                    user = user,
                    email = email,
                    username = username,
                    phone = form.cleaned_data['phone'],
                    address = form.cleaned_data['address']
                )
                messages.success(request, 'Your account has been created!')
                return redirect('customadmin:login_view')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BuyerRegistrationForm()
    return render(request,'register.html', {'form': form})

def vendor_register(request):
    msg = None
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already registered.')
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'This username is already taken.')
            if form.errors:
                # Form is not valid, display error message
                messages.error(request, 'Please correct the errors below.')
            else:
                user = form.save(commit=False)
                user.is_vendor = True
                user.save()
                msg = 'user created'
                vendorid = get_random_string(length=13)
                vendor_profile = VendorProfile.objects.create(
                    user = user,
                    email = email,
                    username = username,
                    phone = form.cleaned_data['phone'],
                    address = form.cleaned_data['address'],
                    vendorid = vendorid
                )
                messages.success(request, 'Your account has been created!')
                return redirect('customadmin:login_view')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = VendorRegistrationForm()
        return render(request,'register.html', {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)
    message = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('customadmin:adminpage')
            elif user is not None and user.is_buyer:
                login(request, user)
                return redirect('buyer:home')
            elif user is not None and user.is_vendor:
                vendor = VendorProfile.objects.get(user=user)
                if vendor.is_locked:
                    messages.warning(request, 'Your Profile is locked!, Contact Admin.')
                    return redirect('customadmin:login_view')
                else:
                    login(request, user)
                    return redirect('vendor:vendor_home')
            else:
                message = 'invalid credentials'
        else:
            message = 'error validating form'
    return render(request, 'login.html', {'form': form, 'message': message})

@login_required(login_url='/login/')
def admin(request):
    if request.user.is_authenticated and request.user.is_admin:
        total_revenue = Order.objects.all().aggregate(Sum('total_price'))
        total_customers = BuyerProfile.objects.count()
        admin_profit = Product.objects.all().aggregate(Sum('admin_profit'))
        orders = Order.objects.order_by('-ordered_at')[:5]
        context = {
            'total_revenue': total_revenue,
            'total_customers': total_customers,
            'admin_profit' : admin_profit,
            'orders': orders,
        }
        return render(request,'admin_index.html', context)
    else:
        return redirect('customadmin:login_view')
    
@login_required(login_url='/login/')
def vendors_list(request):
    if request.user.is_authenticated and request.user.is_admin:
        vendor = VendorProfile.objects.all()
        total_vendors = VendorProfile.get_total_vendors()
        context = {
            'vendor': vendor,
            'total_vendors': total_vendors,
         }
        return render(request, 'vendors_list.html', context)
    else:
        return redirect('customadmin:login_view')
    
@login_required(login_url='/login/')
def toggle_vendor_lock(request, vendor_id):
    vendor = VendorProfile.objects.get(id=vendor_id)
    print(vendor)
    vendor.is_locked = not vendor.is_locked
    vendor.save()
    return redirect('customadmin:vendors_list')

def vendor_check(request):
    logout(request)
    return redirect('vendor:vendor_home')

def logout_view(request):
    logout(request)
    return redirect('customadmin:index')