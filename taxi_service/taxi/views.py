from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from django.http import HttpRequest
from .models import Booking
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user.customer
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'taxi/create_booking.html', {'form': form})

def taxi_list(request):
    taxis = Vehicle.objects.filter(available=True)
    return render(request, 'taxi/taxi_list.html', {'taxis': taxis})

def user_bookings(request):
    bookings = Booking.objects.filter(customer__user=request.user)
    return render(request, 'taxi/user_bookings.html', {'bookings': bookings})

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer__user=request.user)
    return render(request, 'taxi/booking_detail.html', {'booking': booking})

