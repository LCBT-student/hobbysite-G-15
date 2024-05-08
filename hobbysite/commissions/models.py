from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    commission_choices = [
        ('Open','Open'),
        ('Full','Full'),
        ('Completed','Completed'),
        ('Discontinued','Discontinued'),
    ]
    status = models.CharField(max_length=255, choices=commission_choices, default='Open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='author'
    )
    # The project specs did not have Author listed in the Commission model.
    # However, it is heavily implied to be included because of detail view,
    # create view, and update view talking about a commission's owner/author.
    # Most likely, it was just not written in by accident, but I've left this
    # comment here just in case for clarification.

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:commission_detail', args=[self.id])
    

    class Meta:
        ordering = ['created_on']
        verbose_name = 'commission'
        verbose_name_plural = 'commissions'


class Job(models.Model):
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveIntegerField()
    open_manpower = models.PositiveIntegerField(default=10)
    job_choices = [
        ('Open','Open'),
        ('Full','Full'),
    ]
    status = models.CharField(max_length=255, choices=job_choices, default='Open')

    def __str__(self):
        return '{} {}'.format(Commission.title, self.role)

    def get_absolute_url(self):
        return reverse('commission_detail', args=[self.id])
    
    
    class Meta:
        ordering = ['-status','-manpower_required','role']
        verbose_name = 'job'
        verbose_name_plural = 'jobs'


class JobApplication(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    applicant = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='applicant'
    )
    job_apply_choices = [
        ('Pending','Pending'),
        ('Accepted','Accepted'),
        ('Rejected','Rejected')
    ]
    status = models.CharField(max_length=255, choices=job_apply_choices, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-applied_on']
        verbose_name = 'application'
        verbose_name_plural = 'applications'

