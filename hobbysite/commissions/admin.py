from django.contrib import admin
from .models import Commission, Job, JobApplication

# Register your models here.

class CommissionAdmin(admin.ModelAdmin):
    model = [Commission]


class JobAdmin(admin.TabularInline):
    model = [Job]


class JobApplicantAdmin(admin.TabularInline):
    model = [JobApplication]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job)
admin.site.register(JobApplication)