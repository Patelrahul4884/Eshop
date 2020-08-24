from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.customer import Customer

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
                request.session['customer']=customer.id
                return redirect('all')
            else:
                error_message='Email or password invalid!!'
        else:
            error_message='Email or password invalid!!'
        return render(request,'store/login.html',{'error':error_message})


def logout(request):
    request.session.clear()
    return redirect('login')