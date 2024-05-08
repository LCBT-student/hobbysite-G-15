from .models import Commission, Job, JobApplication
from .forms import CommissionForm, LockedJobForm, JobForm, JobApplicationForm

from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

# Create your views here.

class CommissionListView(ListView):
    model = Commission
    template_name = 'commission_list.html'
    context_object_name = 'commissions'


class CommissionDetailView(DetailView, FormMixin):
    model = Commission
    template_name = 'commission_detail.html'
    context_object_name = 'commissions'
    form_class = JobApplicationForm


class CommissionDetail(View):
    def get(self, request, id):
        commission = Commission.objects.get(pk=id).title
        job = Job.objects.filter(commission__title=commission)        
        apply_form = JobApplicationForm

        context = {
            'commission': commission,
            'job': job,
            'apply_form': apply_form
        }
        return render(request, 'commission_detail.html', context)
    

class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commission_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['com_form'] = CommissionForm()
        context['first_job_form'] = LockedJobForm()
        context['job_form'] = JobForm()
        return context
    # Above allows templates to reference the forms
    # This also allows multiple forms in a single view, just
    # dont forget to call it appropriately in the template.
    # *for example, see how commission_add.html calls {%csrf_token%}
    # then calls for {{ comm_form }} and {{ job_form }}, not {{ form }}

    def post(self, request, *args, **kwargs):
        context = {}
        profile = request.user

        if request.method == 'POST':
            com_form = CommissionForm(request.POST)
            job_form = JobForm(request.POST)
            first_job_form = LockedJobForm(request.POST)

            if com_form.is_valid() and first_job_form.is_valid():
                new_com_form = com_form.save(commit=False)
                new_com_form.author = profile
                new_com_form.save()
                new_job_form = first_job_form.save(commit=False)
                new_job_form.commission = new_com_form
                new_job_form.save()
                return redirect('/commissions/list')
            # Above is the creation of a commission + a job
            # the [and] statement is to force a user to create a job for the commission
            elif job_form.is_valid():
                job_form.save()
                return redirect('/commissions/list')
            # Above is only to create a new job
            # *put it in a different <form> in the template to make it work
            # **not filtered, so other users can add jobs to your commission...
            # **its not a part of the specs, so its fine
            else:
                self.object_list = self.get_queryset(**kwargs)
                context = self.get_context_data(**kwargs)
                context['com_form'] = com_form
                context['first_job_form'] = first_job_form
                context['job_form'] = job_form
                return self.render_to_response(context)
        return redirect('/commissions/list')

class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commission_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['com_form'] = CommissionForm()
        return context

    def post(self, request, *args, **kwargs):
        context = {}

        if request.method == 'POST':
            commission_detail = Commission.objects.get(pk=self.kwargs['pk'])

            com_form = CommissionForm(request.POST, instance=commission_detail)
            # ***VERY IMPORTANT: remember to add instance=variable
            # where in variable = model.objects.get(pk=self.kwargs['pk'])
            # This allows the instance to be updated, or it won't work otherwise

            if com_form.is_valid():
                new_com_form = com_form.save(commit=False)
                new_com_form.save()
                return redirect('commissions:commission_detail', pk=commission_detail.pk)
            else:
                self.object_list = self.get_queryset(**kwargs)
                context = self.get_context_data(**kwargs)
                context['com_form'] = com_form
                return self.render_to_response(context)
        return redirect('/commissions/list')
