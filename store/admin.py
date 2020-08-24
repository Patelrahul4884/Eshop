from django.contrib import admin
from .models import Product,Category,Customer
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']    

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)