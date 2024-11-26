from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from customadmin.models import *
from vendor.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from buyer.forms import *
from django.contrib import messages
from django.db import transaction
from collections import defaultdict
from django.db.models import Sum

# Create your views here.

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)

def home(request):
    products = Product.objects.order_by('-created')[:8]
    context = {'products': products}
    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def cart_add(request, product_id):
    print(product_id)
    # product_id = request.POST.get('product_id')
    product = Product.objects.get(id=product_id)
    buyer_profile, created = BuyerProfile.objects.get_or_create(user=request.user)
    cart, created = Cart.objects.get_or_create(user=buyer_profile)
    cart.products.add(product)
    return redirect('buyer:products')

@login_required(login_url='/login/')
def cart_view(request):
    # cart_id = request.cart.cart_id
    buyer_profile, created = BuyerProfile.objects.get_or_create(user=request.user)
    cart, created = Cart.objects.get_or_create(user=buyer_profile)
    items = cart.products.all()
    # print(items)
    for item in items:
        item.subtotal = item.total_price * cart.quantity
    total = sum(item.subtotal for item in items)
    cart.subtotal = total
    cart.save()
    total = sum(item.total_price for item in items)
    # context = {
    #     'items' : items,
    #     'total' : total,
    # }
    return render(request, 'cart.html', {'cart': cart, 'items':items, 'total':total})

@login_required(login_url='/login/')
def cart_remove(request, product_id):
    product = Product.objects.get(id=product_id)
    buyer_profile, created = BuyerProfile.objects.get_or_create(user=request.user)
    cart, created = Cart.objects.get_or_create(user=buyer_profile)
    cart.products.remove(product)
    return redirect('buyer:cart_view')

# def place_order(request):
#     if request.method == 'POST':
#         cart = Cart.object.get(user=request.user)
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.user = request.user
#             order.product = Product.objects.get(id=product_id)
#             order.cart = cart
#             order.quantity = cart.quantity
#             order.total_price = order.product.price * order.quantity
#             print(order.total_price)
#             order.save()
#             order.products.clear()
#             messages.success(request, "Order placed successfully!")
#             return redirect('buyer:home')
#     else:
#         form = OrderForm(request.POST)
#         product = Product.objects.get(id=product_id)
#         initial_data = {'product': product, 'quantity': 1}
#         form = OrderForm(initial=initial_data)
#         order, created = Order.objects.get_or_create(user=request.user)
#         context = {'order':order,'product_id': product_id, 'form': form}
#         return render(request, 'place_order.html', context)

@login_required(login_url='/login/')
@transaction.atomic
def place_order(request):
    buyer_profile, created = BuyerProfile.objects.get_or_create(user=request.user)
    cart = Cart.objects.filter(user=buyer_profile).first()
    if not cart:
        messages.error(request, 'Your cart is empty.')
        return redirect('buyer:cart_view')
    
    vendor_products = defaultdict(list)
    for product in cart.products.all():
        vendor_products[product.vendor].append(product)
    
    for vendor, products in vendor_products.items():
        total_price = sum(product.total_price for product in products)
        order = Order.objects.create(
            user=buyer_profile, 
            cart=cart,
            vendor=vendor,
            quantity=len(products),
            name = buyer_profile.username,
            email = buyer_profile.email,
            phone = buyer_profile.phone,
            address = buyer_profile.address,
            total_price = total_price
        )
        order.products.set(products)
    
    # form = OrderForm(instance=order)
    
    # if request.method == 'POST':
    #     form = OrderForm(request.POST, instance=order)
    #     if form.is_valid():
    # product_id = request.POST.get('product_id')
    # product = Product.objects.get(id=product_id)
    # total_price = cart.subtotal.amount
    
    # order = form.save(commit=False)
    # for product in cart.products.all():
    #     product.add(product)
    #     order.cart = cart
    #     order.quantity = cart.quantity
    
    #     print(f"product price: {product.price}")
    #     print(f"order quantity: {order.quantity}")
    
    #     total_price = total_price
    #     name = request.user.name
    #     email = request.user.email
    # order.phone = form.cleaned_data['phone']
    # order.address = form.cleaned_data['address']
    # order.save()
            
    messages.success(request, 'Your order has been placed.')
    cart.products.clear()
    # cart.update_subtotal()
    return redirect('buyer:order_history')

    # return render(request, 'place_order.html', {'cart': cart,'form': form})

# @login_required
# def place_order(request):
#     cart = get_object_or_404(Cart, user=request.user)
#     order = Order.objects.create(user=request.user, cart=cart, name=request.user.username, email=request.user.email)
#     print(cart, order)
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         # if form.is_valid():
#         #     # total_price = cart.subtotal.amount
#         #     order = form.save(commit=False)
#         #     order.user = request.user
#         #     order.cart = cart
#         #     # product_id = request.POST.get('product_id')
#         #     # product = Product.objects.get(id=product_id)
#         #     order.total_price = cart.subtotal.amount
#         #     order.save()
#         #     order.product.set(cart.products.all())
#         #     order.name = form.cleaned_data['name']
#         #     order.email = form.cleaned_data['email']
#         #     order.phone = form.cleaned_data['phone']
#         #     order.address = form.cleaned_data['address']
#         #     order.save()
#         #     messages.success(request, 'Your order has been placed.')
#         #     cart.products.clear()
#         #     cart.subtotal = 0
#         #     cart.save()
#         return redirect(form)

#     return render(request, 'cart.html')



@login_required(login_url='/login/')
def order_history(request):
    buyer_profile, created = BuyerProfile.objects.get_or_create(user=request.user)
    orders = Order.objects.filter(user=buyer_profile).order_by('-ordered_at')
    context = {
        'orders' : orders,
    }
    return render(request, 'order_history.html', context)