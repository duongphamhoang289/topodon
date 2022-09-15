import django_filters

from .models import *

class TicketFilter(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields = '__all__'