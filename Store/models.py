# from typing_extensions import Required
from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=1000, default = "Không có")
    category = models.CharField(max_length=200, default=None)
    img = models.ImageField(upload_to='uploads/img')
    id = models.CharField(max_length=200, primary_key=True,default=1)
    slug = SlugField(max_length=100, unique=True,default=1)
    discount_price = models.PositiveIntegerField(blank=True, null=True,default=1)
    best_seller = models.BooleanField(default = False)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("product", kwargs={
            'slug': self.slug
        })

class Customer(models.Model):
    name = models.CharField(max_length=10)