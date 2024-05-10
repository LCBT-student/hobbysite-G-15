from typing import Any
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ArticleCategory, Article
from .forms import ArticleForm, CommentForm


class ArticleListView(ListView):
    model = Article
    template_name = 'wiki/article_list.html'

    def get_queryset(self):
        user_profile = self.request.user
        article_catgories= ArticleCategory.objects.all()
        if user_profile.is_authenticated:
            users_articles = Article.objects.filter(author=user_profile)
            other_articles = Article.objects.exclude(author=user_profile)

            return {'users_articles': users_articles, 'other_articles': other_articles, 
                    'categories': article_catgories }
        return {'categories': article_catgories}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.get_queryset().get('categories')
        user_profile = self.request.user
        if user_profile.is_authenticated:
            context['users_articles'] = self.get_queryset().get('users_articles')
            context['other_articles'] = self.get_queryset().get('other_articles')
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki/article_view.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm(initial={'author': self.request.user, 'article': self.get_object()})
        return context
    
    def post(self, request,*args,**kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return self.get(request,*args,**kwargs)

        self.object_list = self.get_queryset(**kwargs)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'wiki/article_create.html'
    redirect_field_name = 'login'

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = self.request.user
        return initial
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form['updated_on'].disabled = True
        form['author'].disabled = True
        form['created_on'].disabled = True
        return form


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'wiki/article_update.html'
    redirect_field_name = 'login'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form['author'].disabled = True
        form['created_on'].disabled = True
        return form

