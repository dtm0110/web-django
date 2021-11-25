from django.shortcuts import render
from Store.models import Product
from Carts.models import CartItem
from django.contrib.auth.decorators import login_required
# Create your views here.

    
@login_required(login_url='/user/login/')   
def cart(request):
    CartItems = CartItem.objects.all()
    return render(request,"cart.html",{'CartItems':CartItems})

@login_required(login_url='/user/login/')
def checkout(request):
    total = 0  
    quantity = 0
    CartItems = CartItem.objects.all()
    for cart_item in CartItems:
        print(cart_item.sub_total)
        total = total + cart_item.sub_total()
        quantity = quantity + cart_item.quantity
    context = {
        'CartItems' : CartItems,
        'total': total,
        'quantity': quantity
    }
    return render(request,"checkout.html",context)

def base(request):
    return render(request, 'home.html');

def single_product(request):
    return render(request,"single-product.html");
