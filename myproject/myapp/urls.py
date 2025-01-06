from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
#Auth
    path('register/',views.register, name='register'),
    path('login/', views.user_login, name='login'),
    #$path('logout/', views.logout_user, name='logout'),

#Search
    path('search_buses/', views.search_buses,name='search_buses'),
    path('book_bus/<int:bus_id>/', views.book_bus, name='book_bus'),
    path('search_hotel/', views.hotel_booking,name='search_hotel'),
    path('book_hotel/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
    path('search_trains/', views.search_trains,name='search_trains'),
    path('book_train/<int:train_id>/', views.book_train, name='book_train'),
    path('search_launches/', views.search_launches,name='search_launches'),
    path('book_launch/<int:launch_id>/', views.book_launch, name='book_launch'),
    path('search_air/', views.search_air,name='search_air'),
    path('book_air/<int:plane_id>/', views.book_air, name='book_air'),
    path('search_cars/', views.search_cars,name='search_cars'),
    path('book_car/<int:car_id>/', views.book_car, name='book_car'),
    path('book/<int:park_id>/', views.book_ticket, name='book_ticket'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),

    #path('payment/', views.payment_page,name='payment'),
    path('payment/', views.payment_page, name='payment_page'),
    path('ticket/<int:booking_id>/', views.ticket_print, name='ticket_print'),
    


]
   

    

