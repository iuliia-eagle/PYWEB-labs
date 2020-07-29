from django.contrib import admin
from .models import *

admin.site.register(Aircraft)
admin.site.register(Seat)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Booking)
admin.site.register(Ticket)
admin.site.register(TicketFlight)
admin.site.register(BoardingPass)

