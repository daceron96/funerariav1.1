from django.urls import path
from .views import ProductOutputListView, ProductOutputCreateView, ProductOutputDetailView

product_output_patterns = ([ 
    path('list/',ProductOutputListView.as_view(), name = 'product_output_list'),
    path('create/',ProductOutputCreateView.as_view(), name = 'product_output_create'),
    path('detail/<int:pk>/',ProductOutputDetailView.as_view(), name='product_output_detail'),
    # path('update/<int:pk>/',ProductInputUpdateView.as_view(), name='product_input_update'),
    # path('deposit/<int:pk>/',ProductInputDepositView.as_view(), name='product_input_deposit'),
    # # path('change/<int:pk>/',ProductChangeState.as_view(), name='product_change'),

    # path('autocomplete-product/',autocomplete_product, name = 'autocomplete_product'),

    # #TODO URL eliminar item de base de datos
    # # path('delete/detail/<int:pk>/',ProductInputDeleteDetailView.as_view(), name='input_detele_detail'),

],'output')