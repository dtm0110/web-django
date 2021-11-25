from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_total = models.FloatField()

    def full_name(self):
        return "{0} {1}".format(self.first_name.title(), self.last_name.title())

    def full_address(self):
        return "{0},  {1}".format(self.address.title(), self.country.title())

    def __str__(self):
        return self.first_name