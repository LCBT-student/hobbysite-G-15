from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=63, default='A Random Person')
    email_address = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
