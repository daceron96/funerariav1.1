from django.urls import path
from .views import ProductLoanListView, ProductLoanCreateview, ProductLoanDetailView
from .functions import filter_loan_by_type

product_loan_patterns = ([ 
    path('list/',ProductLoanListView.as_view(), name = 'product_loan_list'),
    path('create/',ProductLoanCreateview.as_view(), name = 'product_loan_create'),
    path('detail/<int:pk>/',ProductLoanDetailView.as_view(), name='product_loan_detail'),

    path('filter/type/',filter_loan_by_type, name = 'loan_filter_type'),

],'loan')
