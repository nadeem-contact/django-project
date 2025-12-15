from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    phone = models.CharField(max_length=7, default = "123")
    age = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=50, blank=True)

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return self.title
    