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
    path('search_air/', views.search_air,name='search_air'),
    path('book_air/<int:plane_id>/', views.book_air, name='book_air'),

]
   

    

