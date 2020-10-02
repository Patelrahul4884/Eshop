from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.customer import Customer
from store.models.product import Product
from store.models.order import Order

class Checkout(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))

        for product in products:
            order=Order(product=product,customer=Customer(id=customer),quantity=cart.get(str(product.id)),price=product.price,address=address,phone=phone,)
            order.save()
        request.session['cart']={}
        return redirect('orders')