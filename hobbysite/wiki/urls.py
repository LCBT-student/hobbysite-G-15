from django.urls import path

from .views import ArticleDetailView, ArticleListView, ArticleCreateView, ArticleUpdateView

urlpatterns = [
    path('articles', ArticleListView.as_view(), name='category_view'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail_view'),
    path('article/add', ArticleCreateView.as_view(), name='article_create_view'),
    path('article/<int:pk>/edit', ArticleUpdateView.as_view(), name='article_update_view'),
]

app_name = 'wiki'
