from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from user_management.models import Profile
from django.urls import reverse_lazy
from .models import Thread, ThreadCategory
from .forms import ThreadForm, CommentForm

def index(request):
    return HttpResponse('Welcome to the Forum! Check out the threads of posts and ENJOY!!!')


class ThreadListView(ListView):
    model = ThreadCategory
    template_name = 'forum_list.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            author = Profile.objects.get(user=self.request.user)
            data['user_created'] = Thread.objects.filter(author=author)
        return data   


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum_details.html'

    def get_context_data(self, **kwargs):
        thread = self.get_object()
        data = super().get_context_data(**kwargs)
        author = thread.author
        data['form'] = CommentForm(initial={'author': author, 'thread': thread})
        data['thread_owner'] = Thread.objects.filter(author=thread.author)
        data['from_category'] = Thread.objects.filter(category=thread.category)
        if self.request.user.is_authenticated:
            data['user'] = Profile.objects.get(user=self.request.user)
        return data

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        thread = self.get_object()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = Profile.objects.get(user=self.request.user) 
            comment.thread = thread 
            comment.save() 
            return redirect('forum:thread-detail', pk=thread.pk)
        data = self.get_context_data(**kwargs)
        return self.render_to_response(data)
    

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'forum_createview.html'

    def get_success_url(self):
        return reverse_lazy('forum:thread-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        author = Profile.objects.get(user=self.request.user)
        data['form'] = ThreadForm(initial={'author': author})
        return data
    
    def get_initial(self):
        author = Profile.objects.get(user=self.request.user)
        return {'author':author}
    

class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'forum_updateview.html'

    def get_success_url(self):
        return reverse_lazy('forum:thread-detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)