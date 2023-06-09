from django.contrib import admin
from .models import Product, Customer

# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

admin.site.register(Product, ProductModelAdmin)

class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'state', 'mobile']

admin.site.register(Customer, CustomerModelAdmin)