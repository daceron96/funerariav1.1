from django.db import models

from apps.core.models import BaseModel
from apps.supplier.models import Supplier


class ProductCategory(BaseModel):
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        ordering = ['name']
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Product(BaseModel):

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    consecutive = models.SmallIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    @property
    def stock_wait(self):
        from django.db.models import Sum
        quantity = ProductDetail.objects.filter(
            product=self, state=True).aggregate(Sum('stock_wait'))
        if quantity['stock_wait__sum'] == None:
            quantity['stock_wait__sum'] = 0
        return quantity


    @property
    def stock_cellar(self):
        from django.db.models import Sum
        quantity = ProductDetail.objects.filter(
            product=self, state=True).aggregate(Sum('stock_cellar'))
        if quantity['stock_cellar__sum'] == None:
            quantity['stock_cellar__sum'] = 0
        return quantity

    @property
    def stock_loan(self):
        from django.db.models import Sum
        quantity = ProductDetail.objects.filter(
            product=self, state=True).aggregate(Sum('stock_loan'))
        if quantity['stock_loan__sum'] == None:
            quantity['stock_loan__sum'] = 0
        return quantity

    def __str__(self):
        return self.name


class ProductDetail(BaseModel):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    code_list = models.CharField(max_length=1000, blank=True, null=False)
    stock_cellar = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    stock_wait = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    stock_loan = models.PositiveSmallIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['pk']
        verbose_name = "Detalle de producto"
        verbose_name_plural = "Detalles de producto"

    def __str__(self):
        return str(self.pk)
