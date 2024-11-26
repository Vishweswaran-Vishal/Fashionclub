from django.urls import path, include
from . import views
from buyer.views import *
from customadmin.views import *

app_name = 'buyer'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('cart_add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart_remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/', views.cart_view, name='cart_view'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_history/', views.order_history, name='order_history'),
]
