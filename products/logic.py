from products.models import ProductCategory, Product

def index_page_context():
    context = {
        'title': 'Store',
    }
    return context


def products_page_context():
    context = {
        'title': 'Store - Catalog',
        'categories': get_all_categories(),
        'products': get_all_products(),
    }
    return context


def get_all_categories():
    return ProductCategory.objects.all()


def get_all_products():
    return Product.objects.all()
