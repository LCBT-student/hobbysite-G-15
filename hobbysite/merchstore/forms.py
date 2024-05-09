from django import forms
from .models import Product,Transaction

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'stock', 'product_type','status']
        widgets = {
            'product_type': forms.Select(),
            'status': forms.Select(),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['owner'].disabled = True
        

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

