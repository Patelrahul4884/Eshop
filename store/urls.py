from django.urls import path
from .views import index,signup,Login

urlpatterns=[
    path('',index,name='all'),
    path('signup',signup,name='signup'),
    path('login',Login.as_view(),name='login'),
]