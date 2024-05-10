from .forms import ProductForm, TransactionForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Transaction
# from .forms import ProductForm, TransactionForm
from user_management.models import Profile
from user_management import models as ProfileModel
from django.shortcuts import get_object_or_404


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
            
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_object(self, queryset=None):
        """Override get_object to ensure that the object is set."""
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        self.object = obj
        return obj

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        
        # Check if the user is the owner of the product
        if request.user.profile == product.owner:
            # If the user is the owner, redirect to the same page with a message or handle it appropriately
            # You can add a message or do any other action here
            return redirect('merchstore:product_detail', pk=product.pk)
        
        # If the user is not the owner, proceed with processing the transaction
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.product = product
            transaction.buyer = request.user.profile
            transaction.save()
            
            # Update product stock
            product.stock -= transaction.amount
            product.save()
            
            # Redirect the user to the cart or login page based on authentication status
            if request.user.is_authenticated:
                return redirect('merchstore:cart')
            else:
                return redirect('your_login_url')  # Replace 'your_login_url' with your actual login URL
        
        # If form is invalid or other error occurred, render the detail page again
        return self.render_to_response(self.get_context_data(form=form))

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fo_rm'] = ProductForm()  # Pass the instance to prepopulate the form
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        product_detail = Product.objects.get(pk=self.kwargs['pk'])
        form = ProductForm(request.POST,instance = product_detail)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form) 
        
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    # success_url = reverse_lazy('merchstore:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = ProductForm()
        return context
    
    def post(self, request, *args, **kwargs):
        fo_rm = ProductForm(request.POST)
        if fo_rm.is_valid():
            new_merch_form = fo_rm.save(commit=False)
            new_merch_form.owner = request.user.profile
            new_merch_form.save()
            fo_rm.save(commit = False)  
        # Do the Task Creation here, similar to the FBV
            return redirect('merchstore:product_list')
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['product'] = fo_rm
            return self.render_to_response(context)    

class CartView(LoginRequiredMixin, ListView):
    template_name = 'cart_view.html'
    context_object_name = 'grouped_transactions'
    form_class = TransactionForm

    def get_queryset(self):
        transactions = Transaction.objects.filter(buyer=self.request.user.profile)
        grouped_transactions = {}
        for transaction in transactions:
            owner = transaction.product.owner
            if owner in grouped_transactions:
                grouped_transactions[owner].append(transaction)
            else:
                grouped_transactions[owner] = [transaction]
        return grouped_transactions
    
    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            fo_rm = ProductForm(request.POST,initial={'owner': self.request.user})

            if fo_rm.is_valid():
                product_form = fo_rm.save(commit = False)
                product_form.owner=request.user.Profile
                product_form.save()
            # Do the Task Creation here, similar to the FBV
                return redirect('merchstore:product_list')
            else:
                self.object_list = self.get_queryset(**kwargs)
                context = self.get_context_data(**kwargs)
                context['fo_rm'] = fo_rm
                return self.render_to_response(context) 
        
class TransactionListView(LoginRequiredMixin, ListView):
    template_name = 'transaction_list.html'
    context_object_name = 'grouped_transactions'
    form_class = TransactionForm

    def get_queryset(self):
        # Filter transactions where the logged-in user is the owner of the product
        transactions = Transaction.objects.filter(product__owner=self.request.user.profile)
        grouped_transactions = {}
        for transaction in transactions:
            buyer = transaction.buyer  # Corrected to get the buyer of the transaction
            if buyer in grouped_transactions:
                grouped_transactions[buyer].append(transaction)
            else:
                grouped_transactions[buyer] = [transaction]
        return grouped_transactions

    def post(self, request, *args, **kwargs):
        # Handle POST requests here if needed
        pass