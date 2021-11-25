from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

def search(request):
    q = request.GET['q']
    data = Product.objects.filter( name__icontains = q).order_by('id')
    return render(request, 'search.html', {'data': data})
    
def home(request):
    Products = Product.objects.all() 
    return render(request,"home.html", {'Products':Products})

def product(request):
    context = {
        'product' : Product.objects.all()
    }
    return render(request, "single-product.html", context)

class HomeView(ListView):
    model = Product
    template_name = "shop.html"
    context_object_name = 'Products'
    paginate_by = 8

class ProductDetailView(DetailView):
    model = Product
    template_name = "single-product.html"