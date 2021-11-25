from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 

# Create your views here.


class login1(View):
    def get(self,request):
        return render(request,'user/login.html');
    def post(self,request):
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        user = authenticate(username = username1, password= password1)
        if user is None:
            messages.success(request,'Username not found!')
            return redirect('user:login')
        else:
            login(request,user)
            return redirect('/')

class register1(View):
    def get(self,request):
        return render(request,'user/register.html');
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        firstName = request.POST.get('firstname')
        lastName = request.POST.get('lastname')

        if User.objects.filter(username = username).first():
            messages.success(request,"Username is taken!");
            return redirect('user:register');
        user_obj = User.objects.create_user(username = username, first_name=firstName, last_name=lastName, password=password) 
        user_obj.save()
        return redirect('user:login') 

def logout1(request):
    logout(request)
    return redirect('/')
