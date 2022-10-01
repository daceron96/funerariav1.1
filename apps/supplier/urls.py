from django.urls import path

from apps.supplier.views import (SupplierListView,SupplierCreateView,SupplierDetailView,
    SupplierUpdateView,SupplierChangeState)

supplier_patterns = ([ 
    path('supplier/list/',SupplierListView.as_view(), name = 'supplier_list'),
    path('supplier/create/',SupplierCreateView.as_view(), name = 'supplier_create'),
    path('supplier/detail/<int:pk>/',SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier/update/<int:pk>/',SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier/change/<int:pk>/',SupplierChangeState.as_view(), name='supplier_disabled'),

],'supplier')