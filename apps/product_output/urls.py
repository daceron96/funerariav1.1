from django.urls import path
from .views import ProductOutputListView, ProductOutputCreateView, ProductOutputDetailView
from .functions import filter_output_by_type
product_output_patterns = ([ 
    path('list/',ProductOutputListView.as_view(), name = 'product_output_list'),
    path('create/',ProductOutputCreateView.as_view(), name = 'product_output_create'),
    path('detail/<int:pk>/',ProductOutputDetailView.as_view(), name='product_output_detail'),

    path('filter/type/',filter_output_by_type, name = 'output_filter_type'),

],'output')