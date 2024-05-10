from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from user_management.models import Profile 

class Product_type(models.Model):
    name = models.CharField(max_length= 255)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        ordering =['name']
        
    def get_absolute_url(self):
        return reverse('merchstore:product_detail', args=[self.id])   #same name with the html template

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    description = models.CharField(max_length=255)
    stock = models.IntegerField(null=True, default=0)
    owner = models.ForeignKey('user_management.Profile',
        on_delete=models.CASCADE,null= True, default = None)
    product_type = models.ForeignKey(
        Product_type,
        on_delete = models.CASCADE,
        related_name = 'products'
    ) 
    status_choices =(
        ('available', 'Available'),
        ('onsale', 'On Sale'),
        ('outofstock', 'Out of Stock'),
    )
    status = models.CharField(max_length=20, choices = status_choices, default = 'available')
    def get_absolute_url(self):
        return reverse('merchstore:product_detail', args=[self.id])  # Adjusted to match the correct URL name

    class Meta:
        ordering =['product_type', 'name']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
    
    def merchstore_product(self):
        return self.product_type  # Merchstore should have the Product Object as the detail
    
class Transaction(models.Model):
    buyer = models.ForeignKey('user_management.Profile',
        on_delete=models.SET_NULL,
        null =True,
        related_name = 'buyer'
    )
    seller = models.ForeignKey('user_management.Profile',
        on_delete=models.SET_NULL,
        null =True,
        related_name = 'seller'
    )      

    product = models.ForeignKey(Product, 
        on_delete=models.SET_NULL, 
        null=True)
    amount = models.IntegerField()
    status_choices = (
        ('oncart','On Cart'),
        ('topay', 'To Pay'),
        ('toship','To Ship'),
        ('toreceive','To Receive'),
        ('delivered','Delivered'),
    )
    status = models.CharField(max_length=20, choices= status_choices)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.amount} of {self.product.name}"