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
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apply_form'] = JobApplicationForm()
        context['commission'] = Commission
        context['job'] = Job
        context['application'] = JobApplication
        context['open_manpower'] = Job.open_manpower
        return context
    
    def post(self, request, *args, **kwargs):
        context = {}
        apply_form = JobApplicationForm()
        job_form = JobForm()
        com_form = CommissionForm()
        profile = self.request.user

        if request.method == 'POST':
            apply_form = JobApplicationForm(request.POST)

            if apply_form.is_valid():
                application = apply_form.save(commit=False)
                job = request.POST.get('job')
                job_form = JobForm(instance=Job.objects.get(pk=job))
                # Does not need a request.POST since the request is only from
                # clicking a Apply button that only refers to JobApplication
                
                job_manpower = job_form.save(commit=False)
                job_manpower.open_manpower = job_manpower.manpower_required
                signees = JobApplication.objects.filter(job=job_manpower).count()
                manpower_sum = job_manpower.manpower_required - signees
                if manpower_sum <= 0:
                    job_manpower.open_manpower = 0
                    job_manpower.status = "Full"
                else:
                    job_manpower.open_manpower = manpower_sum - 1
                    if job_manpower.open_manpower <= 0:
                        job_manpower.status = "Full"
                accepted_signees = JobApplication.objects.filter(job=job_manpower,status="Accepted").count()
                if accepted_signees >= job_manpower.manpower_required:
                    job_manpower.status = "Complete"
                # for the Accepted status check
                job_manpower.save()
                # Above is about the job's manpower and status change

                application.job = Job.objects.get(pk=job)
                application.applicant = profile
                application.status = "Pending"
                if accepted_signees >= job_manpower.manpower_required:
                    application.status = "Rejected"
                # job only gets set to complete after someone tries to apply
                # to it once (since it requires someone to post/apply)
                # this makes the apply button only disappear when someone
                # tries to apply to a job wherein accepted signees is already
                # at the same number as manpower_required...
                # to adapt to this buggy mess, I just made the first to apply
                # get a rejected status, and the button disappears...
                application.save()
                # Above is about the JobApplication itself

                commission_detail = Commission.objects.get(pk=self.kwargs['pk'])
                com_form = CommissionForm(instance=commission_detail)
                com_status = com_form.save(commit=False)
                for x in Job.objects.filter(commission=commission_detail).all():
                    if x.status != "Full":
                        com_status.save()
                        return redirect('commissions:commission_list')
                com_status.status = "Full"
                com_status.save()
                # Above is commission's status update as seen in 
                # the spec's UpdateView requirement (see the description 
                # about it in CommissionUpdateView's copy of this code)
                # *has to go last because of the return redirect
                # *if it wasnt last, application wouldnt be saved...

                return redirect('commissions:commission_list')
            else:
                return redirect('commissions:commission_list')
                # If there is an error in how it loads, it'll redirect
                # back to avoid seeing an empty version of the page
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['apply_form'] = apply_form
            context['commission'] = Commission
            context['job'] = Job
            context['application'] = JobApplication
            context['open_manpower'] = Job.open_manpower
            return self.render_to_response(context)


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
                new_job_form.open_manpower = new_job_form.manpower_required
                new_job_form.save()
                return redirect('/commissions/list')
            # Above is the creation of a commission + a job
            # the [and] statement is to force a user to create a job for the commission
            elif job_form.is_valid():
                new_job_form = job_form.save(commit=False)
                new_job_form.open_manpower = (
                    job_form.cleaned_data.get('manpower_required')
                )
                new_job_form.save()
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
                for x in Job.objects.filter(commission=commission_detail).all():
                    if x.status != "Full":
                        new_com_form.save()
                        return redirect('commissions:commission_detail', 
                                        pk=commission_detail.pk)
                    # Above checks if all jobs from the commission is full
                    # if atleast one isnt full, it saves and returns early
                new_com_form.status = "Full"
                new_com_form.save()
                return redirect('commissions:commission_detail',
                                pk=commission_detail.pk)
                # if all is full and the for loop ends, it sets the status to full then saves
            else:
                self.object_list = self.get_queryset(**kwargs)
                context = self.get_context_data(**kwargs)
                context['com_form'] = com_form
                return self.render_to_response(context)
        return redirect('/commissions/list')
