from django.db import models
from django.urls import reverse

# Create your models here.

class Commission(models.Model):
    Title = models.CharField(max_length=255)
    Description = models.TextField()
    People_Required = models.PositiveIntegerField()
    Created_On = models.DateTimeField(auto_now_add=True)
    Updated_On = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title
    
    def get_absolute_url(self):
        return reverse('commissions:commission_detail', args=[self.id])
    

    class Meta:
        ordering = ['Created_On']
        verbose_name = 'commission'
        verbose_name_plural = 'commissions'


class Comment(models.Model):
    Commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    Entry = models.TextField()
    Created_On = models.DateTimeField(auto_now_add=True)
    Updated_On = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(Commission.Title, self.Entry)

    def get_absolute_url(self):
        return reverse('commission_detail', args=[self.id])
    
    
    class Meta:
        ordering = ['-Created_On']
        unique_together = ['Created_On', 'Entry']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'