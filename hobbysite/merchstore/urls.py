from django.urls import path
from .views import  Product_typeListView,Product_typeDetailView

urlpatterns = [
    path('items/', Product_typeListView.as_view(), name='product_list'),
    path('item/<int:pk>', Product_typeDetailView.as_view(), name='product_detail'),
]
app_name = 'merchstore'