from django.shortcuts import render
from django.http import HttpResponse
from .models.products import Product
from .models.categories import Category

# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_id(categoryID)
    else:
        products = Product.get_all_products()
    context = {
        "products" : products,
        "categories" : categories
    }
    return render(request, "index.html", context)


def signup(request):
    return render(request, "signup.html")