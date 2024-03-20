from .models import Product,Product_type
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import View

class Product_typeListView(ListView):
    model = Product_type
    template_name = 'product_list.html'
    context_object_name = 'product_types'
    
class Product_typeDetailView(DetailView):
    model = Product_type
    template_name ='product_detail.html'
    context_object_name = 'product_types'


class ProductDetail(View):
     def get(self, request, id):
        product_type = Product_type.get(pk=id).Name
        product = Product.objects.filter(product_type__Name=product_type)
        context = {
            'product_type': product_type,
            'product': product,
        }
        return render(request, 'recipe_detail.html', context)
