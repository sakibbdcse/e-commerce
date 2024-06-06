from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BillingAddress
from .forms import BillingAddressForm
from django.contrib.auth.decorators import login_required

@login_required
def add_billing_address(request):
    form = BillingAddressForm()
    if request.method == 'POST':
        form = BillingAddressForm(request.POST)
        if form.is_valid():
            billing_address = form.save(commit=False)
            billing_address.user = request.user
            billing_address.save()
            messages.success(request, 'Billing address added successfully')
            return redirect('view_cart')  # Redirect to the cart or any other page
    return render(request, 'app_payment/add_billing_address.html', {'form': form})

@login_required
def edit_billing_address(request):
    billing_address = BillingAddress.objects.get(user=request.user)
    form = BillingAddressForm(instance=billing_address)
    if request.method == 'POST':
        form = BillingAddressForm(request.POST, instance=billing_address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Billing address updated successfully')
            return redirect('view_cart')  # Redirect to the cart or any other page
    return render(request, 'app_payment/edit_billing_address.html', {'form': form})
