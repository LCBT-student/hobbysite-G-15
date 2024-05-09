from django.urls import path
from .views import index, ForumListView, ForumDetailView

urlpatterns=[
    path('', index, name='index'),
    path('threads/', ForumListView.as_view(), name='threads'),
    path('thread/<int:pk>', ForumDetailView.as_view(), name='forum-details')
]

app_name='forum'