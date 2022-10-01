from django.db import models
from apps.core.models import BaseModel

class Supplier(BaseModel):
    
    identifier = models.CharField(max_length=50, blank=False, null=False, unique=True)
    name = models.CharField(max_length=50, blank=False,null=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        ordering = ['name']
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
    @property
    def stock_wait(self, *args, **kwargs):
        from apps.product.models import ProductDetail
        from django.db.models import Sum
        print(kwargs)
        quantity = ProductDetail.objects.filter(
            supplier=self, state=True).aggregate(Sum('stock_wait'))
        if quantity['stock_wait__sum'] == None:
            quantity['stock_wait__sum'] = 0
        return quantity


    @property
    def stock_cellar(self):
        from apps.product.models import ProductDetail
        from django.db.models import Sum
        quantity = ProductDetail.objects.filter(
            supplier=self, state=True).aggregate(Sum('stock_cellar'))
        if quantity['stock_cellar__sum'] == None:
            quantity['stock_cellar__sum'] = 0
        return quantity

    @property
    def stock_loan(self):
        from apps.product.models import ProductDetail
        from django.db.models import Sum
        quantity = ProductDetail.objects.filter(
            supplier=self, state=True).aggregate(Sum('stock_loan'))
        if quantity['stock_loan__sum'] == None:
            quantity['stock_loan__sum'] = 0
        return quantity

    def __str__(self):
        return self.name