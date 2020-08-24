from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse
from django.views import View
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
# Create your views here.

def index(request):
    
    categories=Category.get_all_categories()
    categoryId=request.GET.get('category')

    if categoryId:
        products=Product.get_all_products_by_id(categoryId)
    else:
        products=Product.get_all_products()

    ctx={'products':products,'categories':categories}
    return render(request,'store/index.html',ctx)

#validation
def validation(customer):
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

#register user
def registerUser(request):
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
    error_message=validation(customer)
            
    if not error_message:
        customer.password=make_password(customer.password)
        customer.register()
        return redirect('all')
    else:
        data={
            'error':error_message,
            'values':value
        }
        return render(request,'store/signup.html',data)

def signup(request):
    if request.method=='GET':
        return render(request,'store/signup.html')
    else:
        return registerUser(request)

class Login(View):
    def get(self,request):
        return render(request,'store/login.html')

    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)   
        error_message=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                return redirect('all')
            else:
                error_message='Email or password invalid!!'
        else:
            error_message='Email or password invalid!!'
        return render(request,'store/login.html',{'error':error_message})