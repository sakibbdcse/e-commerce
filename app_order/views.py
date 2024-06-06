from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app_order.models import Cart, Order
from app_shop.models import Product

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item, created = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'Quantity updated')
        else:
            order.orderitems.add(order_item)
            messages.info(request, 'New item added to cart')
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item)
        messages.info(request, 'This item was added to your cart')
    return redirect('home')

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user, purchased=False)
    context = {
        'cart_items': cart_items
    }
    return render(request, 'app_order/cart.html', context)