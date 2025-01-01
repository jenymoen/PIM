from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'index.html')

def product_list(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'product_list.html', context)

def product_detail(request,pk):
    product_detail = Product.objects.get(id=pk)
    product_all = Product.objects.all()

    context = {
        'product_detail': product_detail,
        'product_all': product_all
    }

    return render(request, 'product_detailView.html', context)