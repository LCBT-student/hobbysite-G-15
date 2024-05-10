from django.db import models
from django.urls import reverse
from user_management.models import Profile

from time import timezone
import datetime


class ThreadCategory(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    
    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('forum:thread-list', args=[str(self.pk)])
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Thread Category"
        verbose_name_plural = "Thread Categories"


class Thread(models.Model):
    title = models.CharField(max_length=225)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        Profile,
        on_delete = models.SET_NULL,
        related_name = "author",
        null = True
    )
    category = models.ForeignKey(
        ThreadCategory, 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        related_name='categories'
    )
    
    def get_root_url(self):
        return reverse('forum:thread-list')

    def get_absolute_url(self):
        return reverse('forum:thread-detail', args=[self.pk])
    
class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete = models.SET_NULL,
        related_name = "comment_author",
        null = True
        )
    thread = models.ForeignKey(
        Thread,
        on_delete = models.CASCADE,
        related_name = "parent_thread"
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Thread"
        verbose_name_plural = "Threads"
