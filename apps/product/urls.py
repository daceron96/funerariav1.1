from django.urls import path
from apps.product.views import (ProductListView, ProductCreateView, ProductDetailView,
    ProductChangeState, ProductUpdateView, ProductGetView)

product_patterns = ([ 
    path('list/',ProductListView.as_view(), name = 'product_list'),
    path('create/',ProductCreateView.as_view(), name = 'product_create'),
    path('detail/<int:pk>/',ProductDetailView.as_view(), name='product_detail'),
    path('update/<int:pk>/',ProductUpdateView.as_view(), name='product_update'),
    path('change/<int:pk>/',ProductChangeState.as_view(), name='product_change'),
    
    
    path('get/<str:code>/',ProductGetView.as_view(), name='product_get'),

],'product')