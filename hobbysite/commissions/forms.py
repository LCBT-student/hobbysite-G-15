from django import forms

from .models import Commission, Job, JobApplication

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title','description','status']
        

class LockedJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role','manpower_required','status']
    # added this form for the sake of 'locking' it to a commission


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['applied_on']
        exclude = ['applied_on']