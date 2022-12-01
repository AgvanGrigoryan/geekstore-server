from django.http import HttpResponseRedirect

from products.models import ProductCategory, Product, Basket

from django.core.paginator import Paginator


def index_page_context():
    context = {
        'title': 'Store',
    }
    return context


def products_page_context(category_id):
    context = {
        'title': 'Store - Catalog',
        'categories': get_all_categories(),
    }
    return context


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
