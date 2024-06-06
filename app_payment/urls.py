from django.urls import path
from . import views

urlpatterns = [
    path('billing-address/add/', views.add_billing_address, name='add_billing_address'),
    path('billing-address/edit/', views.edit_billing_address, name='edit_billing_address'),
]
