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
    # path('book/<int:park_id>/', views.book_ticket, name='book_ticket'),
    # path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    # path('book/<int:concert_id>/', views.book_ticket, name='book_ticket'),
    # path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),


    #path('payment/', views.payment_page,name='payment'),
    path('payment/', views.payment_page, name='payment_page'),
    path('ticket/<int:booking_id>/', views.ticket_print, name='ticket_print'),


    path('adminn_dashboard/', views.adminn_dashboard, name='adminn_dashboard'),
    path('ad_add_bus/', views.ad_add_bus, name='ad_add_bus'),
    path('ad_edit_bus/<int:bus_id>/', views.ad_edit_bus, name='ad_edit_bus'),
    path('ad_delete_bus/<int:bus_id>/', views.ad_delete_bus, name='ad_delete_bus'),
    path('adminn_plane/', views.adminn_plane, name='adminn_plane'),
    path('ad_add_plane/', views.ad_add_plane, name='ad_add_plane'),
    path('ad_edit_plane/<int:plane_id>/', views.ad_edit_plane, name='ad_edit_plane'),
    path('ad_delete_plane/<int:plane_id>/', views.ad_delete_plane, name='ad_delete_plane'),




    path('adminn_hotel/', views.adminn_hotel, name='adminn_hotel'),
    path('ad_add_hotel/', views.ad_add_hotel, name='ad_add_hotel'),
    path('ad_edit_hotel/<int:hotel_id>/', views.ad_edit_hotel, name='ad_edit_hotel'),
    path('ad_delete_hotel/<int:hotel_id>/', views.ad_delete_hotel, name='ad_delete_hotel'),

    path('adminn_car/', views.adminn_car, name='adminn_car'),
    path('ad_add_car/', views.ad_add_car, name='ad_add_car'),
    path('ad_edit_car/<int:car_id>/', views.ad_edit_car, name='ad_edit_car'),
    path('ad_delete_car/<int:car_id>/', views.ad_delete_car, name='ad_delete_car'),


    # #Park

    # path('adminn_car/', views.adminn_car, name='adminn_car'),
    # path('ad_add_car/', views.ad_add_car, name='ad_add_car'),
    # path('ad_edit_car/<int:car_id>/', views.ad_edit_car, name='ad_edit_car'),
    # path('ad_delete_car/<int:car_id>/', views.ad_delete_car, name='ad_delete_car'),


    #Events
    path('adminn_event/', views.adminn_event, name='adminn_event'),
    path('ad_add_event/', views.ad_add_event, name='ad_add_event'),
    path('ad_edit_event/<int:event_id>/', views.ad_edit_event, name='ad_edit_event'),
    path('ad_delete_event/<int:event_id>/', views.ad_delete_event, name='ad_delete_event'),

    
    
    #Train


    path('adminn_train/', views.adminn_train, name='adminn_train'),
    path('ad_add_train/', views.ad_add_train, name='ad_add_train'),
    path('ad_edit_train/<int:train_id>/', views.ad_edit_train, name='ad_edit_train'),
    path('ad_delete_train/<int:train_id>/', views.ad_delete_train, name='ad_delete_train'),



    #Launch


    path('adminn_launch/', views.adminn_launch, name='adminn_launch'),
    path('ad_add_launch/', views.ad_add_launch, name='ad_add_launch'),
    path('ad_edit_launch/<int:launch_id>/', views.ad_edit_launch, name='ad_edit_launch'),
    path('ad_delete_launch/<int:launch_id>/', views.ad_delete_launch, name='ad_delete_launch'),




]
   

    

