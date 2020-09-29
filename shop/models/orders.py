from django.db import models
from .products import Product
from .customers import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=50, default='')
    order_id = models.CharField(max_length=50, default='')
    order_date = models.DateField(default=datetime.datetime.today)
    order_status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-order_date')