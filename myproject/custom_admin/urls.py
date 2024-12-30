# custom_admin/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard route
    path('users/', views.manage_users, name='manage_users'),  # Manage users route
    path('buses/', views.manage_buses, name='manage_buses'),  # Manage buses route
    path('bookings/', views.manage_bookings, name='manage_bookings'),  # Manage bookings route
]
