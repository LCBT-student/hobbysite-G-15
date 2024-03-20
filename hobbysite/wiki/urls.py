from django.urls import path

from .views import ArticleDetailView, ArticleListView

urlpatterns = [
    path('articles', ArticleListView.as_view(), name='category_view'),
    path('article/<int:pk>', ArticleDetailView.as_view(),
         name='article_detail_view')
]

app_name = 'wiki'
