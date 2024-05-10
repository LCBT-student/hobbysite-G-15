from django.urls import path

from .views import CreateUserProfile, UpdateUserProfile


urlpatterns = [
    path('profile/', UpdateUserProfile.as_view(), name="update_user_profile"),
    path('/accounts/register', CreateUserProfile.as_view(), name="create_user_profile")
]

app_name = "user_management"