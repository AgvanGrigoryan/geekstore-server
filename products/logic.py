from django.http import HttpResponseRedirect

from products.models import ProductCategory, Product, Basket

from django.core.paginator import Paginator


def index_page_context():
    context = {
        'title': 'Store',
    }
    return context


def products_page_context(category_id, page):
    context = {
        'title': 'Store - Catalog',
        'categories': get_all_categories(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = get_all_products()
    products_paginator = create_products_paginator(products, page)
    print(type(products_paginator.number))
    context.update({'products': products_paginator})
    return context


def create_products_paginator(products, page):
    paginator = Paginator(products, 3)
    return paginator.page(page)


def get_all_categories():
    return ProductCategory.objects.all()


def get_all_products():
    return Product.objects.all()


def create_basket_or_plus(request, product_id, current_page):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)
