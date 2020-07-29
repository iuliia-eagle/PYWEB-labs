from airtrans.models import Flight, Seat, Ticket, TicketFlight, BoardingPass

# Список рейсов между двумя аэропортами
Flight.objects.all().filter(departure_airport__airport_name="Пашковский",arrival_airport__airport_name="Пулково")

# Список мест для выбранного самолёта
Seat.objects.all().filter(aircraft_code__model="Airbus 320")

# Список выданных посадочных талонов для выбранного перелёта
BoardingPass.objects.all().filter(flight_id__flight_no='1')

# Список имён пассажиров данного рейса
Ticket.objects.all().filter(ticket_no__in=tickets).values('passenger_name')
