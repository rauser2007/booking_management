from django.contrib import admin
from .models import Driver, Vehicle, Ride, Customer, Booking, Payment, Route, Tariff

# Register your models here.
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Ride)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Route)
admin.site.register(Tariff)