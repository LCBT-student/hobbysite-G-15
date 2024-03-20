from django.db import models
from django.urls import reverse

class Product_type(models.Model):
    Name = models.CharField(max_length= 255)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.Name
    class Meta:
        ordering =['Name']
    def get_absolute_url(self):
        return reverse('merchstore:product_detail', args=[self.pk])   #same name with the html template

class Product(models.Model):
    Name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    Description= models.CharField(max_length=255)
    product_type = models.ForeignKey(
        Product_type,
        on_delete = models.CASCADE,
        related_name = 'products'
    ) 
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])

    class Meta:
        ordering =['product_type']