from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def display_home(request):
    return render(request, 'ProductManagerApp/products.html')
