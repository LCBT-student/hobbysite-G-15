from django import forms

from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'created_on', 'updated_on', 'title', 'category', 'header_image', 'entry']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'article', 'created_on', 'updated_on', 'entry']