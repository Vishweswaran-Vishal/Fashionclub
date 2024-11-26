from django.urls import path, include
from . import views

app_name = 'vendor'

urlpatterns = [
    path('vendor/home/', views.vendor_home, name='vendor_home'),
    path('vendor/product_new/', views.product_new, name='product_new'),
    path('vendor/product_delete/<int:id>/', views.product_delete, name='product_delete'),  
    path('vendor/product_edit/<int:id>/', views.product_edit, name='product_edit'),  
    path('vendor_orders', views.vendor_orders, name='vendor_orders'),  
]