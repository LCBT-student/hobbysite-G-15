from django.contrib import admin

from .models import Article, ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    model = Article

    search_fields = ('title',)
    list_filter = ['created_on', 'updated_on', 'category__name']
    fieldsets = [
        ('Details', {
            'fields': [
                ('title', 'category'), ('created_on', 'updated_on'), 'entry'
            ]
        })
    ]


class ArticleInline(admin.TabularInline):
    model = Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInline,]

    search_fields = ('name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
