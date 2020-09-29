"""BuyNow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views.index import Index
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import Checkout, clear_cart
from .views.orders import Orders
from shop.middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('signup/', Signup.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', logout, name="logout"),
    path('cart/',auth_middleware(Cart.as_view()), name="cart"),
    path('checkout/', Checkout.as_view(), name="checkout"),
    path('clear/', clear_cart, name="clear"),
    path('orders/',auth_middleware( Orders.as_view()), name="orders")
]
