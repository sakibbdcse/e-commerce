from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app_shop.models import Product

class Home(ListView):
    model = Product
    template_name = 'app_shop/home.html'
    context_object_name = 'products'

class ProductDetails(DetailView):
    model = Product
    template_name = 'app_shop/product_details.html'
