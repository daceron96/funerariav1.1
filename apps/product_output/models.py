from email.policy import default
from lib2to3.pytree import Base
from unittest.util import _MAX_LENGTH
from django.db import models
from apps.core.models import BaseModel
from apps.product.models import Product
class OutputType(BaseModel):
    name = models.CharField(max_length = 50, blank = False, null = False)
    class Meta:
        verbose_name = "Tipo de salida"

    def __str__(self):
        return f'{self.name}'

class ProductOutput(BaseModel):

    reference = models.CharField(max_length = 50, blank = False, null = False, unique = True)
    output_type = models.ForeignKey(OutputType, on_delete = models.CASCADE)
    identifier = models.CharField(max_length = 50, blank = False, null = False)
    name_client = models.CharField(max_length = 50, blank = False, null = False)
    description = models.TextField(max_length = 1000, blank = True)
    price_total = models.PositiveIntegerField(default=0)
    quantity = models.PositiveSmallIntegerField(default = 0,blank=False, null=False)
    invoice_number = models.CharField(max_length = 50, blank = False, null = False, unique = True)
    class Meta:
        verbose_name = "Salida"
        ordering = ['-id']

    def __str__(self):
        return f'{self.reference}'

class OutputDetail(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank = False, null=False)
    code_list = models.CharField(max_length=3000, blank=True,default='')
    product_output = models.ForeignKey(ProductOutput, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Detalle salida"

    def __str__(self):
        return f'{self.product.name}'

    