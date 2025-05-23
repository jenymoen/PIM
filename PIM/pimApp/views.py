from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ShopifySettings, Suppliers
from .forms import ShopifySettingsForm, ProductForm
import requests


def dashboard(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'dashboard.html', context)


def index(request):
    return render(request, 'index.html')

def product_list(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'product_list.html', context)

def product_detail(request,pk):
    product = get_object_or_404(Product, pk=pk)
    product_detail = Product.objects.get(id=pk)
    product_all = Product.objects.all()

    context = {
        'product_detail': product_detail,
        'product_all': product_all,
        'product': product,
    }

    return render(request, 'product_detailView.html', context)


def push_product_to_shopify(requests, pk):
    product = get_object_or_404(Product, pk=pk)
    product.push_to_shopify()
    return redirect('product_detail', pk=pk)
# Compare this snippet from PIM/pimApp/views.py:

def update_shopify_settings(request):
    shopify_settings, created = ShopifySettings.objects.get_or_create(pk=1)
    if request.method == 'POST':
        form = ShopifySettingsForm(request.POST, instance=shopify_settings)
        if form.is_valid():
            form.save()
            return redirect('update_shopify_settings')
    else:
        form = ShopifySettingsForm(instance=shopify_settings)
    return render(request, 'settings.html', {'form': form})

def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'new_product.html', {'form': form})

def supplier_list(request):
    suppliers = Suppliers.objects.all()
    context = {
        'suppliers': suppliers
    }

    return render(request, 'suppliers_list.html', context)