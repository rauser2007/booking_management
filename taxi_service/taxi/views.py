from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from .models import Vehicle

# Create your views here.

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'taxi/creat_booking.html', {'form': form})

def taxi_list(request):
    taxis = Vehicle.objects.filter(available=True)
    return render(request, 'taxi/taxi_list.html', {'taxis': taxis})