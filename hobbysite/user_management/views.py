from django.views.generic.edit import UpdateView
from.models import Profile

# Create your views here.

class UserUpdateView(UpdateView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'
