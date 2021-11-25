from django.shortcuts import render, redirect
from Store.models import Product
from .models import  CartItem
from django.contrib.auth.decorators import login_required

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    is_exists_cart_item = CartItem.objects.filter(product=product).exists()
    if is_exists_cart_item:
                    cart_item = CartItem.objects.get(
                        product=product)
                    cart_item.quantity += 1
                    cart_item.save()
                    print(cart_item.quantity)
    else:
                cart_item = CartItem.objects.create(
                    product=product,
                    quantity=1
                )
                cart_item.save()    
    return redirect('cart')

def remove_cart(request, product_id, cart_item_id):
    product = Product.objects.get(id=product_id)
    is_exists_cart_item = CartItem.objects.filter(product=product).exists()
    if is_exists_cart_item:
                    item = CartItem.objects.get(product=product)
                    if item.quantity >= 2:
                        item.quantity -= 1
                        item.save()
                        print(item.quantity)
                    else:
                        item.delete()
    return redirect('cart')

def remove_cart_item(request, product_id, cart_item_id):
    product = Product.objects.get(id=product_id)
    item = CartItem.objects.get(
        product=product)
    item.delete()
    return redirect('cart')


@login_required(login_url='/user/login/') 
def cart(request, total=0, quantity=0):
    total = 0
    CartItems  = CartItem.objects.all()
    return render(request, 'cart.html',{'CartItems' : CartItems})
def shop(request):
    return render(request, 'shop.html')