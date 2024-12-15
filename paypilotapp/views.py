from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.http import require_GET as re_ge

# Create your views here.

@re_ge
def home(request):

    return render(request, 'paypilotapp/home.html')