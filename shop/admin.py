from django.contrib import admin
from shop.models import Product,Brand


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'currency', 'category', 'price', 'photo', 'brand')

class BrandAdmin(admin.ModelAdmin):
    pass






admin.site.register(Product,ProductAdmin)
admin.site.register(Brand,BrandAdmin)

