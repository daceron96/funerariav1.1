from django import forms
from apps.supplier.models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['identifier', 'name', 'phone']

        error_messages = {
            'identifier': {
                'unique': "Ya existe un producto registrado con este mismo identificador."
            },
        }