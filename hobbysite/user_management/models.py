from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
<<<<<<< HEAD
# from user_management.models import Profile

=======
>>>>>>> 13409faed6575bd7f2e46678cae18c8e539cefbe


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    name = models.CharField(max_length=50)
    short_bio = models.TextField()
=======

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=63, default='A Random Person')
    email_address = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
>>>>>>> commissions
=======
    display_name = models.CharField(max_length=63)
    email = models.EmailField()
>>>>>>> 13409faed6575bd7f2e46678cae18c8e539cefbe
