from django.urls import path

from .views import (ProductInputListView,ProductInputCreateView, ProductInputDetailView, ProductInputUpdateView,
    ProductInputDepositView)
from .functions import autocomplete_product

product_input_patterns = ([ 
    path('list/',ProductInputListView.as_view(), name = 'product_input_list'),
    path('create/',ProductInputCreateView.as_view(), name = 'product_input_create'),
    path('detail/<int:pk>/',ProductInputDetailView.as_view(), name='product_input_detail'),
    path('update/<int:pk>/',ProductInputUpdateView.as_view(), name='product_input_update'),
    path('deposit/<int:pk>/',ProductInputDepositView.as_view(), name='product_input_deposit'),
    # path('change/<int:pk>/',ProductChangeState.as_view(), name='product_change'),

    path('autocomplete-product/',autocomplete_product, name = 'autocomplete_product'),

    #TODO URL eliminar item de base de datos
    # path('delete/detail/<int:pk>/',ProductInputDeleteDetailView.as_view(), name='input_detele_detail'),

],'input')