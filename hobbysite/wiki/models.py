from django.db import models
from django.urls import reverse
from django.utils import timezone

from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category')
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wiki:category_view')

    @property
    def articles(self):
        return Article.objects.filter(category__name=self.name)

    class Meta:
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='article'
    )
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='article',
        limit_choices_to={'is_staff': True},
    )
    entry = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    header_image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wiki:article_detail_view', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='comment'
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comment'
    )
    entry = models.TextField()
    created_on = models.DateField(default=timezone.now)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['created_on']
