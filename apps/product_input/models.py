from email.policy import default
from lib2to3.pytree import Base
from django.db import models
from apps.core.models import BaseModel
from apps.supplier.models import Supplier
from apps.product.models import Product

class ProductInput(BaseModel):

    reference = models.CharField(max_length=50, blank=False,null=False,unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default = 0,blank=False, null=False)
    in_wait = models.BooleanField(default=True)
    created_qr = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    image_qr = models.CharField(max_length = 100, blank = True) 
    class Meta:
        ordering = ['-in_wait','-id'] 
        verbose_name = "Entrada de producto"
        verbose_name_plural = "Entradas de producto"
    
    def __str__(self):
        return str(self.reference)

#TODO falta poner campos para la creacion y asignacion de la lista de codigos y lo mismo en el modelo principal
class InputDetail(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_input = models.ForeignKey(ProductInput, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(blank=False, null=False)
    code_list = models.CharField(max_length = 1000, default='')
    class Meta:
        
        verbose_name = "Detalle de entrada"
    def __str__(self):
        return f'{self.id}'