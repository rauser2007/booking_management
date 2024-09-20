from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.create_booking, name='create_booking'),
    path('taxis/', views.taxi_list, name='taxi_list'),
]
