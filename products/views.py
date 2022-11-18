from django.shortcuts import render

from products.logic import products_page_context, index_page_context


def index(request):
    context = index_page_context()
    return render(request, 'products/index.html', context)


def products(request):
    context = products_page_context()
    return render(request, 'products/products.html', context)
