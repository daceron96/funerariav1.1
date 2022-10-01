from django import forms
from apps.product.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code', 'name', 'category', 'description']

        error_messages = {
            'code': {
                'unique': "Ya existe un producto registrado con este mismo código."
            },
        }
