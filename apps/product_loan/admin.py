from django.contrib import admin
from .models import ProductLoan, LoanType, LoanDetail

admin.site.register(ProductLoan)
admin.site.register(LoanType)
admin.site.register(LoanDetail)