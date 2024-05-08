from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


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
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='article'
    )
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='article',
    )
    entry = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    header_image = models.ImageField(upload_to='images/', null=True)

    @property
    def article_comments(self):
        return Comment.objects.filter(article__title=self.title).order_by('-created_on')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wiki:article_detail_view', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    author = models.ForeignKey(
        User,
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
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']
