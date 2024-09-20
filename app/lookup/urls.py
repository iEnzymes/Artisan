"""
URL mapping for the user API.
"""
from django.urls import path

from lookup import views


app_name = 'lookup'

urlpatterns = [
    path('services/', views.ServicesView.as_view(), name='services'),
]
