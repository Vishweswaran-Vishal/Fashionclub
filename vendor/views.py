from django.shortcuts import render,  redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from customadmin.models import VendorProfile
from .models import *
from buyer.models import *
from django.urls import reverse
from customadmin.models import *
from .forms import ProductForm
from django.contrib.auth import authenticate, login, get_user_model

# Create your views here.

def vendor_home(request):
    if request.user.is_authenticated and request.user.is_vendor:
        # Get the VendorProfile instance associated with the user
        vendor_profile = VendorProfile.objects.get(user=request.user)
        vendorid = vendor_profile.vendorid
        products = Product.objects.filter(vendor__user=request.user)
        print(vendorid)
        # Render the vendor dashboard template with the vendor_id
        return render(request, 'vendor_index.html', {'vendorid': vendorid, 'products': products})
    else:
        return render(request, 'vendor_index.html')

@login_required(login_url='/login/')
def product_new(request):
    msg = ''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print("form is valid")
            product = form.save(commit=False)
            product.vendor = VendorProfile.objects.get(user=request.user)
            product.admin_profit = (product.vendor_price * Decimal(5))/ Decimal(100)  # calculate admin profit
            product.gst = (product.vendor_price * Decimal(18))/ Decimal(100)  # calculate GST
            product.total_price = product.vendor_price + product.admin_profit + product.gst  # calculate total price
            print(product.total_price)
            print('Saving product to database...')
            product.save()
            msg = 'Product Added!'
            return redirect(reverse('vendor:vendor_home'))
    else:
        form = ProductForm()
    return render(request, 'product_new.html', {'form': form, 'msg':msg})

@login_required(login_url='/login/')
def product_edit(request, id):
    product = get_object_or_404(Product, id=id, vendor__user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('vendor:vendor_home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_edit.html', {'form': form})

@login_required(login_url='/login/')
def product_delete(request, id):
    product = get_object_or_404(Product, id=id, vendor__user=request.user)
    product.delete()
    # messages.success(request, 'The product has been deleted.')
    return redirect('vendor:vendor_home')
    # return render(request, 'product_list.html', {'product': product})

@login_required(login_url='/login/')
def vendor_orders(request):
    vendor_profile = request.user.vendor_profile
    orders = Order.objects.filter(vendor=vendor_profile)
    context = {
        'orders': orders,
    }
    return render(request, 'vendor_orders.html', context)

