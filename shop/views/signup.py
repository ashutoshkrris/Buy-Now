from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  make_password
from shop.models.customers import Customer
from django.views import  View
import re


class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        value = {
            'fname': fname,
            'lname': lname,
            'phone': phone,
            'email': email,
            'password': password
        }

        customer = Customer(fname=fname,
                            lname=lname,
                            phone=phone,
                            email=email,
                            password=password
                            )

        error_msg = self.validate_signup(customer)

        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('index')
        else:
            data = {
                'error': error_msg,
                'value': value
            }
            return render(request, "signup.html", data)

    def validate_signup(self,customer):
        error_msg = None

        # First Name
        if not customer.fname:
            error_msg = "First Name is required."
        elif len(customer.fname) < 2:
            error_msg = "First Name cannot be less than 2 characters."

        # Last Name
        elif not customer.lname:
            error_msg = "Last Name is required."
        elif len(customer.lname) < 2:
            error_msg = "Last Name cannot be less than 2 characters."

        # Phone Number
        elif not customer.phone:
            error_msg = "Phone Number is required."
        elif len(customer.phone) != 10:
            error_msg = "Phone number must be of 10 digits only."

        # Email
        elif not customer.email:
            error_msg = "Email is required."
        elif customer.doesExist():
            error_msg = "Email is already registered."

        # Password
        elif not customer.password:
            error_msg = "Password is required."
        elif customer.password:
            regex = re.compile(
                r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%&_])(?=\S+$).{8,20}$')
            if not regex.match(customer.password):
                error_msg = "Password must be 8 to 20 characters long and must contain atleast one lower case, one uppercase, one special character(@,#,$,%,&,_) and one digit."

        return error_msg
