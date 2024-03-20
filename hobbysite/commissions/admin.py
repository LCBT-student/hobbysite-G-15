from django.contrib import admin
from .models import Commission, Comment

# Register your models here.

class CommissionAdmin(admin.ModelAdmin):
    model = [Commission]


class CommentAdmin(admin.TabularInline):
    model = [Comment]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment)