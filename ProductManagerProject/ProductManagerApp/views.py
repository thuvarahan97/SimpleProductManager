from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product
import csv


# Create your views here.

def product_list(request):
    context = {'product_list': Product.objects.all()}
    return render(request, 'ProductManagerApp/product_list.html', context)


def product_form(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'ProductManagerApp/product_form.html', {'form': form})
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            with open('ProductManagerApp/storage/product_list.txt', 'a+', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=form.cleaned_data.keys())
                writer.writerow({'id': form.cleaned_data['id'], 'name': form.cleaned_data['name'],
                                 'price': '$' + str(format(form.cleaned_data['price'], '.2f'))})
            return redirect('/add_product?result=success')
        else:
            return redirect('/add_product?result=failed')


def product_delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('/')


def search_product(request):
    search_query = request.GET.get('search_query')
    if search_query != "":
        context = {'product_list': Product.objects.all().filter(name__contains=search_query)}
        return render(request, 'ProductManagerApp/product_list.html', context)
    else:
        return redirect('/')
