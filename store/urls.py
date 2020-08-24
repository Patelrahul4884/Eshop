from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.login import Login, logout 
from .views.cart import Cart

urlpatterns=[
    path('',Index.as_view(),name='all'),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('cart',Cart.as_view(),name='cart'),
    path('logout',logout,name='logout'),
]