from django.contrib import admin
from .models import User, Bus, BusBooking, TripHistory


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'firstname', 'lastname', 'username', 'phone', 'email', 'dob', 'gender', 'nid')
    search_fields = ('firstname', 'lastname', 'username', 'phone', 'email', 'nid')
    list_filter = ('gender',)
    ordering = ('-dob',)
    list_per_page = 10


class BusAdmin(admin.ModelAdmin):
    list_display = ('bus_id', 'bus_name', 'departure_location', 'destination_location', 'bus_type', 'fare', 'total_seats', 'available_seats')
    search_fields = ('bus_name', 'departure_location', 'destination_location', 'bus_id')
    list_filter = ('bus_type',)
    ordering = ('bus_name',)
    list_per_page = 10


class BusBookingAdmin(admin.ModelAdmin):
    list_display = ('bus_book_id', 'user', 'bus', 'passenger_name', 'passenger_phone', 'selected_seats')
    search_fields = ('bus_book_id', 'passenger_name', 'user__username', 'bus__bus_name')
    list_filter = ('bus__bus_type', 'user__gender')
    ordering = ('-bus__journey_date',)
    list_per_page = 10


class TripHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'bus', 'journey_date', 'trip_start_time', 'trip_arrival_time', 'status', 'total_fare')
    search_fields = ('user__username', 'bus__bus_name', 'status')
    list_filter = ('status',)
    ordering = ('-journey_date',)
    list_per_page = 10


admin.site.register(User, UserAdmin)
admin.site.register(Bus, BusAdmin)
admin.site.register(BusBooking, BusBookingAdmin)
admin.site.register(TripHistory, TripHistoryAdmin)
