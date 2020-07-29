from django.db import models


class Aircraft(models.Model):
    aircraft_code = models.CharField(max_length=32, primary_key=True)
    model = models.CharField(max_length=100, default='')
    range = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.model}'


class Seat(models.Model):
    seat_no = models.CharField(max_length=32)
    aircraft_code = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    fare_conditions = models.CharField(max_length=100)

    class Meta:
        unique_together = (('aircraft_code', 'seat_no'),)

    def __str__(self):
        return f'{self.aircraft_code} - {self.seat_no}'


class Airport(models.Model):
    airport_code = models.PositiveIntegerField(primary_key=True)
    airport_name = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    coordinates = models.CharField(max_length=100, default='')
    timezone = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.airport_name}'


class Flight(models.Model):
    flight_id = models.PositiveIntegerField(primary_key=True)
    flight_no = models.CharField(max_length=100, default='')
    scheduled_departure = models.DateTimeField()
    scheduled_arrival = models.DateTimeField()
    departure_airport = models.ForeignKey(Airport, related_name='departure_airport', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport, related_name='arrival_airport', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='')
    aircraft_code = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    actual_departure = models.DateTimeField(null=True)
    actual_arrival = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.flight_no}'


class Booking(models.Model):
    book_ref = models.CharField(max_length=100, primary_key=True)
    book_date = models.DateField()
    total_amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.book_ref}'


class Ticket(models.Model):
    ticket_no = models.PositiveIntegerField(primary_key=True)
    book_ref = models.ForeignKey(Booking, on_delete=models.CASCADE)
    passenger_id = models.CharField(max_length=100)
    passenger_name = models.CharField(max_length=100)
    contact_data = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.ticket_no}'


class TicketFlight(models.Model):
    ticket_no = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    fare_conditions = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()

    class Meta:
        unique_together = (('flight_id', 'ticket_no'),)

    def __str__(self):
        return f'{self.flight_id} - {self.ticket_no}'


class BoardingPass(models.Model):
    ticket_no = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    flight_id = models.ForeignKey(Flight,on_delete=models.CASCADE)
    boarding_no = models.CharField(max_length=30)
    seat_no = models.CharField(max_length=30)

    class Meta:
        unique_together = (('flight_id', 'ticket_no'),)

    def __str__(self):
        return f'{self.flight_id} - {self.ticket_no}'










