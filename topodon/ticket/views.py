from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.db.models import Q

from .models import *
from .filters import TicketFilter, DepartmentFilter

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
    # Find ticket by date
    # tickets = Ticket.objects.filter(date_created__year=2022, date_created__month=9, date_created__day=16)
    # Find ticket by customer phone
    # customer_by_phone = Customer.objects.filter(phone='876543210')
    # tickets = Ticket.objects.filter(customer=customer_by_phone[0])
    # Find ticket by ticket id
    # tickets = Ticket.objects.filter(id=3)
    # Find ticket by department id
    # tickets = Ticket.objects.filter(department_id=3)
    # Find ticket by department name
    # department_id_by_name = Department.objects.filter(name="HR")
    # tickets = Ticket.objects.filter(department_id=department_id_by_name[0])
    my_filter = TicketFilter(request.GET, queryset=tickets)
    tickets = my_filter.qs
    return render(request, 'ticket/ticket.html', {'tickets': tickets, 'my_filter': my_filter})

def department(request):
    departments = Department.objects.all()
    my_filter = DepartmentFilter(request.GET, queryset=departments)
    departments = my_filter.qs
    # Find department by name
    # departments = [Department.objects.get(name='Marketing')]
    # Find department by id
    #departments = [Department.objects.get(id=1)]
    return render(request, 'ticket/department.html', {'departments': departments, 'my_filter': my_filter})