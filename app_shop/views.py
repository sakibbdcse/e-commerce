from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from app_shop.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'app_shop/home.html'
    context_object_name = 'products'

class ProductDetails(DetailView):
    model = Product
    template_name = 'app_shop/product_details.html'

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    
    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'name': product.name,
            'price': product.price,
            'quantity': 1,
            'image': product.mainimage.url,
        }
    
    request.session['cart'] = cart
    return redirect('home')