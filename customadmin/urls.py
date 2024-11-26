from django.urls import path, include
from customadmin.views import *
from customadmin import views

app_name = 'customadmin'

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('vendor.urls')),
    path('', include('buyer.urls')),
    path('adminpage/register', views.admin_register, name='adminpage_register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('vendorslist/', views.vendors_list, name='vendors_list'),
    path('vendor/', views.vendor_check, name='vendor'),
    path('vendorslist/<int:vendor_id>/toggle_lock/', views.toggle_vendor_lock, name='toggle_vendor_lock'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    # path('adminpage/register/', views.admin_register, name='admin_register'),
    path('buyer/register/', views.buyer_register, name='buyer_register'),
    path('seller/register/', views.vendor_register, name='vendor_register'),
]