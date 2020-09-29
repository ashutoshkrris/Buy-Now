from django.shortcuts import redirect
from shop.models.customers import Customer
from django.views import View
from shop.models.products import Product
from shop.models.orders import Order
from datetime import datetime


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        order_id = datetime.now().strftime('%Y%m%d%H%M%S')
        products = Product.get_products_by_id(list(cart.keys()))
       
        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          order_id=order_id,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')

def clear_cart(request):
    request.session['cart'] = {}
    return redirect('cart')