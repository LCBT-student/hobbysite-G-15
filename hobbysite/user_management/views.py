from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from.models import Profile

from django.shortcuts import render, redirect

# Create your views here.

class UserUpdateView(UpdateView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

class HomepageListView(ListView):
    model = Profile
    template_name = 'homepage.html'
    