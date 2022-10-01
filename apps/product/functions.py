from math import prod
from django.http import JsonResponse

from .models import Product

def filter_product_name(request):

	if request.GET:
		term = request.GET.get('term')

		query = Product.objects.filter(name__icontains = term)
		product_list = []
		for product in query:
			data = {
				'state' : product.state,
				'id' : product.id,
				'code' : product.code,
				'name' : product.name,
				'category' : product.category.name,
				'stock_cellar' :product.stock_cellar['stock_cellar__sum'],
				'stock_wait' : product.stock_wait['stock_wait__sum'],
				'stock_loan' : product.stock_loan['stock_loan__sum'],
			}
			product_list.append(data)
		return JsonResponse({'data':product_list},status = 200)

		