from .models import Product
from django.shortcuts import render


def main(request):
    products = Product.objects.all()
    context={'products': products}
    return render(request,'main.html',context)


















