from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app_order.models import Cart, Order
from app_shop.models import Product

@login_required
def view_cart(request):
    order = Order.objects.filter(user=request.user, ordered=False).first()
    context = {
        'order': order
    }
    return render(request, 'app_order/cart.html', context)

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Cart, id=pk, user=request.user, purchased=False)
    item.delete()
    messages.info(request, 'Item removed from cart')
    return redirect('view_cart')

@login_required
def checkout(request):
    order = Order.objects.filter(user=request.user, ordered=False).first()
    if order:
        order.ordered = True
        order.save()
        messages.success(request, 'Order placed successfully!')
        return redirect('home')
    messages.warning(request, 'No items in your cart to checkout')
    return redirect('view_cart')

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
def increase_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            order_item.quantity += 1
            order_item.save()
            messages.info(request, f"{item.name} quantity has been updated")
        else:
            messages.info(request, f"{item.name} is not in your cart")
            return redirect('home')
    else:
        messages.info(request, "You don't have an active order")
    return redirect('view_cart')

@login_required
def decrease_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, f"{item.name} quantity has been updated")
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.info(request, f"{item.name} has been removed from your cart")
        else:
            messages.info(request, f"{item.name} is not in your cart")
            return redirect('home')
    else:
        messages.info(request, "You don't have an active order")
    return redirect('view_cart')
