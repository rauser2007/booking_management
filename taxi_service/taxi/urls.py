from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.create_booking, name='create_booking'),
    path('taxis/', views.taxi_list, name='taxi_list'),
    path('bookings/', views.user_bookings, name='user_bookings'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('booking/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('booking/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]
