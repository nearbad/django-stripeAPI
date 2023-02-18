from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.urls import reverse
import stripe

from django.conf import settings
from .models import *


stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    return HttpResponse('<h4 style="text-align: center; margin: 30;">Welcome</h4>')


def buy_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(item.price*100),
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('main:index'))

    )
    return JsonResponse({'session_id': session.id})


def get_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item,
        'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, 'main/get_item.html', context)


def create_order(request, item_ids):
    item_ids_list = item_ids.split(',')
    items = Item.objects.filter(id__in=item_ids_list)
    total_price = sum([item.price for item in items])
    discount = None
    tax = None
    if request.GET.get('discount'):
        discount = get_object_or_404(Discount, pk=request.GET.get('discount'))
        total_price -= discount.amount
    if request.GET.get('tax'):
        tax = get_object_or_404(Tax, pk=request.GET.get('tax'))
        total_price *= (1 + tax.rate)
    order = Order.objects.create(total_price=total_price, discount=discount, tax=tax)
    order.items.set(items)
    line_items = []
    for item in items:
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(item.price*100),
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
            },
            'quantity': 1,
        })
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri(reverse('main:index'))
    )
    return JsonResponse({'session_id': session.id})


def get_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    context = {
        'item': order.items,
        'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, 'main/get_item.html', context)
