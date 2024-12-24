from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('search_buses/', views.search_buses, name='search_buses'),
    path('book/<int:bus_id>/', views.book_bus, name='book_bus'),
    path('payment/<int:booking_id>/', views.payment_page, name='payment_page'),
    path('confirm_payment/<int:booking_id>/', views.confirm_payment, name='confirm_payment'),
    path('payment_success/<int:booking_id>/', views.payment_success, name='payment_success'),
    path('search_air/', views.search_air, name='search_air'),
    path('book/<int:plane_id>/', views.book_air, name='book_air'),
    
    path('car_rentals/', views.car_rentals, name='car_rentals'),
    path('hotel_booking/', views.hotel_booking, name='hotel_booking'),
    path('book/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
    path('book/<int:rent_id>/', views.book_car, name='book_car'),
    path('book/<int:launch_id>/', views.book_launch, name='book_launch'),
]
   

    

