from django.db import models
from django.urls import reverse

# Create your models here.

class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:commission_detail', args=[self.id])
    

    class Meta:
        ordering = ['created_on']
        verbose_name = 'commission'
        verbose_name_plural = 'commissions'


class Comment(models.Model):
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(Commission.title, self.entry)

    def get_absolute_url(self):
        return reverse('commission_detail', args=[self.id])
    
    
    class Meta:
        ordering = ['-created_on']
        unique_together = ['created_on', 'entry']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'