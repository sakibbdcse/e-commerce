from django.shortcuts import render
from django.views.generic import ListView
from app_shop.models import Product

# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'app_shop/home.html'
    context_object_name = 'products'
