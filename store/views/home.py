from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
# Create your views here.


class Index(View):
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        categories=Category.get_all_categories()
        categoryId=request.GET.get('category')

        if categoryId:
            products=Product.get_all_products_by_id(categoryId)
        else:
            products=Product.get_all_products()

        ctx={'products':products,'categories':categories}
        return render(request,'store/index.html',ctx)

    def post(self,request):
        product=request.POST.get('product')
        cart=request.session.get('cart')
        remove=request.POST.get('remove')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]= quantity+ 1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        return redirect('all')
