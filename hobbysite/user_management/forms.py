from django import forms

from .models import Profile

<<<<<<< HEAD
=======

>>>>>>> 13409faed6575bd7f2e46678cae18c8e539cefbe
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'username', 'password', 'display_name']