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
    redirect_field_name = "/accounts/login"