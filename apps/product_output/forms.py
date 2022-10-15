from django import forms
from .models import ProductOutput

class ProductOutputForm(forms.ModelForm):
    class Meta:
        model = ProductOutput
        fields = ['reference', 'output_type', 'identifier', 'name_client','description','price_total','invoice_number']

        error_messages = {
            'reference': {
                'unique': "Ya existe una salida registrada con esta referencia",
                'invoice_number' : "Ya existe un recibo de pago registrado con este número"
            },
        }
