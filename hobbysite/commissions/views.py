from .models import Commission, Comment
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import View

# Create your views here.

class CommissionListView(ListView):
    model = Commission
    template_name = 'commission_list.html'
    context_object_name = 'commissions'


class CommissionDetailView(DetailView):
    model = Commission
    template_name = 'commission_detail.html'
    context_object_name = 'commissions'


class CommissionDetail(View):
    def get(self, request, id):
        commission = Commission.objects.get(pk=id).title
        comment = Comment.objects.filter(commission__title=commission)
        context = {
            'commission': commission,
            'comment': comment
        }
        return render(request, 'commission_detail.html', context)