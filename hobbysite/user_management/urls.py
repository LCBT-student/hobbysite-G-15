from django.urls import path
from .views import UserUpdateView, HomepageListView


urlpatterns = [
    path('update', UserUpdateView.as_view(), name='profile'),
    path('', HomepageListView.as_view(), name='homepage')
]
app_name = "user_management"