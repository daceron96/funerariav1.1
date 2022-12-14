from django.urls import path
from apps.product.views import (ProductListView, ProductCreateView, ProductDetailView,
    ProductChangeState, ProductUpdateView, SearchProductCodeView, ProductGetView, TotalProducts)
from .functions import filter_product_name, filter_product_by_category

product_patterns = ([ 
    path('list/',ProductListView.as_view(), name = 'product_list'),
    path('create/',ProductCreateView.as_view(), name = 'product_create'),
    path('detail/<int:pk>/',ProductDetailView.as_view(), name='product_detail'),
    path('update/<int:pk>/',ProductUpdateView.as_view(), name='product_update'),
    path('change/<int:pk>/',ProductChangeState.as_view(), name='product_change'),
    path('total/',TotalProducts.as_view(), name='product_total'),
    
    path('search/code/', SearchProductCodeView.as_view(), name='search_code'),
    path('get/<str:code>/',ProductGetView.as_view(), name='product_get'),
    path('filter/name/',filter_product_name, name = 'product_filter_name'),
    path('filter/category/',filter_product_by_category, name = 'product_filter_category'),

],'product')