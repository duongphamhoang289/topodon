from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('customer/', views.customer),
    path('ticket/', views.ticket),
    path('department/', views.department),
]