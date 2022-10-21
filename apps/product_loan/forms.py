from django import forms
from .models import ProductLoan

class ProductLoanForm(forms.ModelForm):

	class Meta:
		model = ProductLoan
		fields = ['reference', 'loan_type', 'identifier', 'name_client', 'description']
		error_messages = {
			'reference': {
				'unique': "Ya existe una salida registrada con esta referencia",
				},
			}
