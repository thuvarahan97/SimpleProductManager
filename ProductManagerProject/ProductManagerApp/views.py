from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Products


# Create your views here.

def product_list(request):
    context = {'product_list': Products.objects.all()}
    return render(request, 'ProductManagerApp/products.html', context)


def product_form(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'ProductManagerApp/product_form.html', {'form': form})
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


def product_delete(request, id):
    product = Products.objects.get(pk=id)
    product.delete()
    return redirect('/')


def search_product(request):
    search_query = request.GET.get('search_query')
    if search_query != "":
        context = {'product_list': Products.objects.all().filter(name__contains=search_query)}
        return render(request, 'ProductManagerApp/products.html', context)
    else:
        return redirect('/')