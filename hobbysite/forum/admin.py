from django.contrib import admin
from .models import Thread, ThreadCategory, Comment

class ThreadInline(admin.TabularInline):
    model = Thread

class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory 
    inlines = [ThreadInline,]


class ThreadAdmin(admin.ModelAdmin):
    model = Thread

    search_fields = [
        "title",
    ]
    list_display = ["title", "category", "created_on", "updated_on"]
    list_filter = [
        "created_on",
        "updated_on",
    ]

    fieldsets = [("Details", {"fields": [("title", "entry"), "category"]})]

class CommentInline(admin.TabularInline):
    model = Comment


admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
