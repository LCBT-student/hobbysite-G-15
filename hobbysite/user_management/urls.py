from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 13409faed6575bd7f2e46678cae18c8e539cefbe

from .views import CreateUserProfile, UpdateUserProfile


urlpatterns = [
    path('profile/', UpdateUserProfile.as_view(), name="update_user_profile"),
    path('/accounts/register', CreateUserProfile.as_view(), name="create_user_profile")
]

<<<<<<< HEAD
=======
from .views import UserUpdateView 


urlpatterns = [
    path('', UserUpdateView.as_view(), name='profile'),    
]
>>>>>>> commissions
=======
>>>>>>> 13409faed6575bd7f2e46678cae18c8e539cefbe
app_name = "user_management"