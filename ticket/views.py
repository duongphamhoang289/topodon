from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .filters import TicketFilter

# Create your views here.
def home(request):
    return render(request, 'ticket/index.html')

def login(request):
    return render(request, 'ticket/login.html')

def customer(request):
    customers = Customer.objects.all()
    return render(request, 'ticket/customer.html', {'customers': customers})

def ticket(request):
    tickets = Ticket.objects.all()
    my_filter = TicketFilter()
    return render(request, 'ticket/ticket.html', {'tickets': tickets})

def department(request):
    departments = Department.objects.all()
    return render(request, 'ticket/department.html', {'departments': departments})