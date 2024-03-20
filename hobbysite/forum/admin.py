from django.contrib import admin
from .models import Post, PostCategory


class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory
    
    search_fields = ["name"]
    list_display = ["name"]
    
    fieldsets = [("Details", {"fields": ("name", "description")})]


class PostAdmin(admin.ModelAdmin):
    model = Post

    search_fields = [
        "title",
    ]
    list_display = ["title", "category", "created_on", "updated_on"]
    list_filter = [
        "created_on",
        "updated_on",
    ]

    fieldsets = [("Details", {"fields": [("title", "entry"), "category"]})]


admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
