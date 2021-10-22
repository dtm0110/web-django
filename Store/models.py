from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=20)
    category = models.CharField(max_length=200)
    img = models.ImageField(upload_to='uploads/img')

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=10)