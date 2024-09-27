from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=10)
    year = models.IntegerField()
    color = models.CharField(max_length=30)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"

class Ride(models.Model):
    start_address = models.CharField(max_length=255)
    end_address = models.CharField(max_length=255)
    ride_time = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ride from {self.start_address} to {self.end_address}"

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    start_datetime = models.DateTimeField()  # Час початку бронювання
    end_datetime = models.DateTimeField()  # Час завершення бронювання
    pickup_location = models.CharField(max_length=255)  # Місце початку поїздки
    dropoff_location = models.CharField(max_length=255)  # Місце закінчення поїздки
    taxi = models.ForeignKey(Vehicle, on_delete=models.CASCADE)  # Зв'язок з транспортом (таксі)
    status = models.CharField(max_length=20, choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Canceled', 'Canceled')])

    def __str__(self):
        return f"Booking for {self.customer}"


class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[('Cash', 'Cash'), ('Card', 'Card')])
    payment_status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.booking}"

class Route(models.Model):
    route_name = models.CharField(max_length=255)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    travel_time = models.TimeField()

    def __str__(self):
        return self.route_name

class Tariff(models.Model):
    tariff_name = models.CharField(max_length=50)
    price_per_km = models.DecimalField(max_digits=5, decimal_places=2)
    minimum_price = models.DecimalField(max_digits=5, decimal_places=2)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return self.tariff_name