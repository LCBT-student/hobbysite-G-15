from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
<<<<<<< HEAD
<<<<<<< HEAD
from .models import Profile

# Define an inline admin descriptor for Profile model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    # verbose_name_plural = 'Profile' 

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'short_bio')  # Customize the fields displayed in the admin list view

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register the Profile model with the Django admin
admin.site.register(Profile, ProfileAdmin)
=======

from .models import Profile

# Register your models here.

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInLine,]
=======

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]
>>>>>>> 13409faed6575bd7f2e46678cae18c8e539cefbe


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
<<<<<<< HEAD
>>>>>>> commissions
=======
>>>>>>> 13409faed6575bd7f2e46678cae18c8e539cefbe
