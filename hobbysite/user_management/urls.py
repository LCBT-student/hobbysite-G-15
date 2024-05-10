from django.urls import path
<<<<<<< HEAD

from .views import CreateUserProfile, UpdateUserProfile


urlpatterns = [
    path('profile/', UpdateUserProfile.as_view(), name="update_user_profile"),
    path('/accounts/register', CreateUserProfile.as_view(), name="create_user_profile")
]

=======
from .views import UserUpdateView 


urlpatterns = [
    path('', UserUpdateView.as_view(), name='profile'),    
]
>>>>>>> commissions
app_name = "user_management"