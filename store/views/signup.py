from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer


class Signup(View):
    def get(self,request):
        return render(request,'store/signup.html')
    
    def post(self,request):
        postData=request.POST
        first_name=postData.get('firstname')
        last_name=postData.get('lastname')
        phone=postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')
            
        value={
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email,
        }
        customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
        error_message=self.validation(customer)
                
        if not error_message:
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data={
                'error':error_message,
                'values':value
            }
            return render(request,'store/signup.html',data)

        #validation
    def validation(self,customer):
        error_message=None
        if (not customer.first_name):
            error_message='First name required!!'
        elif not customer.last_name:
            error_message='Last name required!!'
        elif not customer.phone:
            error_message='phone number required!!'
        elif len(customer.phone)<10:
            error_message='phone number must be of 10 digits!!'
        elif not customer.email:
            error_message='email id required!!'
        elif not customer.password:
            error_message='password required!!'
        elif customer.isExist():
            error_message='Email address already exist!!'