from django.db import models
from apps.core.models import BaseModel
from apps.product.models import Product

class LoanType(BaseModel):
	name = models.CharField(max_length = 50, blank = False, null = False)
	class Meta:
		verbose_name = "Tipo de prestamo"

	def __str__(self):
		return f'{self.name}'


class ProductLoan(BaseModel):

	reference = models.CharField(max_length=50, blank=False,null=False,unique=True)
	loan_type = models.ForeignKey(LoanType, on_delete = models.CASCADE)
	identifier = models.CharField(max_length = 50, blank = False, null = False)
	name_client = models.CharField(max_length = 50, blank = False, null = False)
	in_wat = models.BooleanField(default = True)
	quantity = models.PositiveSmallIntegerField(default = 0,blank=False, null=False)
	description = models.TextField(max_length = 1000, blank = True)
	
	class Meta:
		verbose_name = "Prestamo de producto"
		ordering = ['-id']
		
	def __str__(self):
		return f'{self.reference}'

class LoanDetail(BaseModel):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(blank = False, null=False)
	code_list = models.CharField(max_length=3000, blank=True,default='')
	product_loan = models.ForeignKey(ProductLoan, on_delete = models.CASCADE)

	class Meta:
		verbose_name = "Detalle de prestamo"

	def __str__(self):
		return f'{self.product.name}'