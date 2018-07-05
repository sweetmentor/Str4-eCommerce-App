from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrderForm, MakePaymentForm
from product.models import Product
from decimal import Decimal
from cart.utils import get_cart_items_and_total
from django.utils import timezone
from .models import OrderLineItem
from django.contrib import messages
from cart.utils import get_cart_items_and_total
from .utils import save_order_items, charge_card, send_confirmation_email
import stripe
from django.conf import settings

# Create your views here.
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)    
        payment_form = MakePaymentForm(request.POST)
        print(payment_form.errors)
        if order_form.is_valid() and payment_form.is_valid():
            print("******ODER AND PAYMENT VALID")
            # Save The Order
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
        
            # Save the Order Line Items
            cart = request.session.get('cart', {})
            save_order_items(order, cart)
        
            # Charge the Card
            items_and_total = get_cart_items_and_total(cart)
            total = items_and_total['total']
            stripe_token=payment_form.cleaned_data['stripe_id']

            try:
                customer = charge_card(stripe_token, total)
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")

                # Send Email
                send_confirmation_email(request.user.email, request.user, items_and_total)
        
                #Clear the Cart
                del request.session['cart']
                return redirect("/")
    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        context = {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE }
        cart = request.session.get('cart', {})
        cart_items_and_total = get_cart_items_and_total(cart)
        context.update(cart_items_and_total)
    
        return render(request, "checkout/checkout.html", context)

