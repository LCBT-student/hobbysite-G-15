from django.db import models
from django.urls import reverse

from time import timezone
import datetime


class PostCategory(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    
    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Post Category"
        verbose_name_plural = "Post Categories"


class Post(models.Model):
    title = models.CharField(max_length=225)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        PostCategory, 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        related_name='posts'
    )
    
    def get_root_url(self):
        return reverse('forum:threads')

    def get_absolute_url(self):
        return reverse('forum:forum-details', args=[self.pk])
    
    
    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
