from django.urls import path
from .views import CustomLoginView, register, protected_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('protected/', protected_view, name='protected'),
]