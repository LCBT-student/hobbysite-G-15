<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 13409faed6575bd7f2e46678cae18c8e539cefbe
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile
from .forms import ProfileForm

class CreateUserProfile(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = "registration/create_user.html"


class UpdateUserProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "registration/update_user.html"
<<<<<<< HEAD
    redirect_field_name = "/accounts/login"
=======
from django.views.generic.edit import UpdateView
from.models import Profile

# Create your views here.

class UserUpdateView(UpdateView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'
>>>>>>> commissions
=======
    redirect_field_name = "/accounts/login"
>>>>>>> 13409faed6575bd7f2e46678cae18c8e539cefbe
