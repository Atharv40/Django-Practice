from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    manufacture_date = models.DateTimeField()  
    expiry_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} {self.price} {self.manufacture_date} {self.expiry_date}"


class Student(models.Model):
    name = models.CharField(max_length=150)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} {self.address} {self.dob} {self.phone_number})"


class Laptop(models.Model):
    brand = models.CharField(max_length=100)  
    model_name = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)  
    ram_size = models.PositiveIntegerField()  
    storage_capacity = models.PositiveIntegerField() 
    screen_size = models.DecimalField(max_digits=4, decimal_places=1) 
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.model_name} {self.processor}  {self.ram_size} {self.storage_capacity}  {self.screen_size} {self.price})"
