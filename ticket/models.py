from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.name

class Ticket(models.Model):
    department_id = models.ForeignKey(Department, max_length=200, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, max_length=200, null=True, on_delete=models.SET_NULL)
    opinion = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField()
    date_resolved = models.DateTimeField()
    solution = models.CharField(max_length=200, null=True, blank=True)
    STATUS =(
        ('Not Resolvef', 'Not Resolved'),
        ('Resolved', 'Resolved'),
    )
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.opinion
