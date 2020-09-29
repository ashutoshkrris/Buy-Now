from django.contrib import admin
from .models.products import Product
from .models.categories import Category
from .models.customers import Customer
from .models.orders import Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['fname','lname','phone','email','last_logged_in_at']


class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer','quantity','price','order_id','order_date','order_status']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)

admin.site.site_header = 'Buy Now Administrations'