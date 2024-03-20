from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ArticleCategory, Article


class ArticleListView(ListView):
    model = ArticleCategory

    template_name = 'wiki/article_list.html'


class ArticleDetailView(DetailView):
    model = Article

    template_name = 'wiki/article_view.html'
