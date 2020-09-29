from django.http import request
from django.shortcuts import render, redirect
from shop.models.products import Product
from shop.models.categories import Category
from django.views import View

# Create your views here.


class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_id(categoryID)
        else:
            products = Product.get_all_products()
        context = {
            "products": products,
            "categories": categories
        }
        return render(request, "index.html", context)

    def post(self, request):
        product = request.POST['product']
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}   
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('index')