from django.db import models
from datetime import datetime

class Customer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    last_logged_in_at = models.DateTimeField(auto_now=True)

    def register(self):
        self.save()

    @staticmethod
    def get_customer(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False

    @staticmethod
    def update_time(email):
        try:
            customer = Customer.objects.get(email = email)
            customer.last_logged_in_at = datetime.now()
            customer.save()
        except:
            pass


    def doesExist(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return False

    def __str__(self):
        return self.email