from django.http import JsonResponse

from .models import Product, ProductDetail

def serialize_data(query):
		product_list = []
		for product in query:
				data = {
						'state': product.state,
						'id': product.id,
						'code': product.code,
						'name': product.name,
						'category': product.category.name,
						'stock_cellar': product.stock_cellar['stock_cellar__sum'],
						'stock_wait': product.stock_wait['stock_wait__sum'],
						'stock_loan': product.stock_loan['stock_loan__sum'],
				}
				product_list.append(data)
		return product_list

def filter_product_name(request):

		if request.GET:
				term = request.GET.get('term')

				query = Product.objects.filter(name__icontains=term)
				product_list = serialize_data(query)
				return JsonResponse({'data': product_list}, status=200)

def filter_product_by_category(request):
	
	if request.GET:
		pk = request.GET.get('pk')
		if(pk != '-1'):
			query = Product.objects.filter(category__id = pk)
		else:
			query = Product.objects.all()
		product_list = serialize_data(query)
		return JsonResponse({'data': product_list}, status=200)


def validate_list(product_list: list):

	error = {}
	index_list = {}

	for product in product_list:
		try:
			product_code = product['code_list'][0]
			index_code = product_code.index('-')
			code = product_code[0:(index_code)]
			index_identifier = product_code.index('|')
			identifier = product_code[(index_identifier+1):len(product_code)]

			detail = ProductDetail.objects.get(product__code = code, supplier__identifier = identifier)
			code_list = eval(detail.code_list)
			index_list[detail.id] = []
			for code in product['code_list']:
				try:
					index = code_list.index(code)
					index_list[detail.id].append(code)
				except:
					error['code'] = "Codigo invalido"
					break
		except:
			error['code'] = "Codigo de producto invalido"
	return error, index_list
