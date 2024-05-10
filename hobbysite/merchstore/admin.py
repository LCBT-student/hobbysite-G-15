from django.contrib import admin
from .models import Product_type, Product, Transaction


@admin.register(Product_type)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    # Add any other configurations you desire

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'price', 'stock', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'description')
    # Add any other configurations you desire

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'product', 'amount', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ('buyer__display_name', 'product__name')
    # Add any other configurations you desire


