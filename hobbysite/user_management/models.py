from django.db import models
from django.contrib.auth.models import User
# from user_management.models import Profile



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField()