from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# from .form import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# def user_login(request):
#     form = LoginForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         user = authenticate(username=cd['username'], password=cd['password'])
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponse('Đăng nhập thành công')
#             else:
#                 return HttpResponse('Tài khoản không tồn tại')
#         else:
#             return HttpResponse('Tài khoản không hợp lệ')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form':form})
    
# @login_required
# def dashboard(request):
#     return render(request, 'account/dashboard.html', { 'section': 'dashboard'})

""" def base(request):
    return render(request, 'home.html')
def shop(request):
    return render(request, 'shop.html')
def single_product(request):
    return render(request, 'single-product.html')
def cart(request):
    return render(request, 'cart.html')
def checkout(request):
    return render(request, 'checkout.html') """