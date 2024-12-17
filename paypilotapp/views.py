from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.http import require_GET as re_ge
from .models import product

# Create your views here.

@re_ge
def home(request):

    return render(request, 'paypilotapp/home.html')

@re_ge
def products(request):
    pro = product.objects.filter(is_ver=True)[:20]
    context = {
        'products': pro
    }
    return render(request, 'paypilotapp/products.html', context=context)

@re_ge
def exchange(request):

    return render(request, 'paypilotapp/exchange.html')

@re_ge
def binaceslot(request):

    return render(request, 'paypilotapp/binaceslot.html')

@re_ge
def spot(request):

    return render(request, 'paypilotapp/spots.html')