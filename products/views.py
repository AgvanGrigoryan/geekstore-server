from django.http import HttpResponseRedirect
from django.shortcuts import render

from products.logic import products_page_context, index_page_context, create_basket_or_plus
from products.models import Basket

from django.contrib.auth.decorators import login_required


def index(request):
    context = index_page_context()
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = products_page_context(category_id, page)
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id=None):
    current_page = request.META.get('HTTP_REFERER')
    return create_basket_or_plus(request, product_id, current_page)


@login_required
def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
