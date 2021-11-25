from django.shortcuts import render
from django.shortcuts import render
from Carts.models import CartItem
from .forms import ContactForm
import datetime

def place_order(request):
    total = 0  
    quantity = 0
    CartItems = CartItem.objects.all()
    for cart_item in CartItems:
        print(cart_item.sub_total)
        total = total + cart_item.sub_total()
        quantity = quantity + cart_item.quantity
    CartItems  = CartItem.objects.all()
    yr = int(datetime.date.today().strftime('%Y'))
    dt = int(datetime.date.today().strftime('%d'))
    mt = int(datetime.date.today().strftime('%m'))
    d = datetime.date(yr, mt, dt) 
    current_date = d.strftime("%d/%m/20%y")
    body = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'city':form.cleaned_data['city'],
                'phone': form.cleaned_data['phone'],
                'address' : form.cleaned_data['address'],
                'CartItems' : CartItems,
                'total': total,
                'quantity': quantity,
                'date':current_date
            }
    for cart_item in CartItems:
        cart_item.delete()
    return render(request,'pay.html',body)

def pay(request):
    return render(request, 'pay.html')