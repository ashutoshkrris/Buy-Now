from django.shortcuts import render
from django.views import View
from shop.models.orders import Order

class Orders(View):
    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request , 'orders.html'  , {'orders' : orders})