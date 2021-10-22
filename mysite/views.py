from django.shortcuts import render
from Store.models import Product
from Carts.models import CartItem
# Create your views here.
def home(request):
    Products = Product.objects.all() 
    return render(request,"home.html",{'Products':Products})
def cart(request):
    CartItems = CartItem.objects.all()
    return render(request,"cart.html",{'CartItems':CartItems})

def base(request):
    return render(request, 'home.html')
def shop(request):
    return render(request, 'shop.html')
def single_product(request):
    return render(request, 'single-product.html')
""" def cart(request):
    return render(request, 'cart.html') """
def checkout(request):
    return render(request, 'checkout.html')