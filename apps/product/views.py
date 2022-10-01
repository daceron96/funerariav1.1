from math import prod
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import JsonResponse
from apps.product.models import Product, ProductCategory, ProductDetail
from apps.product.forms import ProductForm

# Create your views here.
class ProductListView(ListView):
	model = Product
	template_name = 'product/product_list.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["categories"] = ProductCategory.objects.filter().values('id','name')
		return context
		

class ProductDetailView(DetailView):
	model = Product
	def get(self, *args, **kwargs):
		supplier_list = []
		query = ProductDetail.objects.filter(product = self.get_object())
		for detail in query:
			data = {
				'identifier' : detail.supplier.identifier,
				'name' : detail.supplier.name,
				'stock_cellar' : detail.product.stock_cellar['stock_cellar__sum'],
				'stock_wait' : detail.product.stock_wait['stock_wait__sum'],
				'stock_loan' : detail.product.stock_loan['stock_loan__sum'],
			}
			supplier_list.append(data)

		return JsonResponse({
			'id' : self.get_object().id,
			'state' : self.get_object().state,
			'code' : self.get_object().code,
			'name' : self.get_object().name,
			'category' : self.get_object().category.name,
			'created_date' : self.get_object().created_date,
			'supplier_list' : supplier_list
		})

class ProductCreateView(CreateView):
	model = Product
	form_class = ProductForm
	def post(self,request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save()
			response = JsonResponse({
				'id':form.instance.id,
				'code':form.instance.code,
				'name':form.instance.name,
				'category':form.instance.category.name,
			})
			response.status_code = 200
		else:
			response = JsonResponse({'error':form.errors})
			response.status_code = 400
		return response
		
class ProductUpdateView(UpdateView):
	model = Product
	form_class = ProductForm
	def get(self, *args, **kwargs):
		return JsonResponse({
			'id': self.get_object().id,
			'code': self.get_object().code,
			'name': self.get_object().name,
			'description': self.get_object().description,
			'category': self.get_object().category.id,
		}, status = 200)

	def post(self, *args, **kwargs):
		form = self.form_class(self.request.POST, instance = self.get_object())
		if form.is_valid():
			form.instance.code = self.get_object().code
			form.save()
			return JsonResponse({
				'id' : form.instance.id,
				'name' : form.instance.name,
				'category' : form.instance.category.name,
			}, status = 200)
		return JsonResponse({'error': form.errors},status = 400)


class ProductChangeState(View):

	def post(self, *args, **kwargs):
		pk = self.kwargs['pk']

		try:
			product = Product.objects.get(id = pk)
			product.state = False if product.state else True
			product.save()
			return JsonResponse({'id':pk, 'state':product.state},status = 200)
		except:
			return JsonResponse({'error':"El proveedor no existe"},status = 400 )

class ProductGetView(View):


	def get(self, *args, **kwargs):
		code = self.kwargs['code']
		try:
			product = Product.objects.get(code = code)

			return JsonResponse({
				'id' : product.id,
				'code' : product.code,
				'name' : product.name
			},status = 200)
		except:
			return JsonResponse({'error':{'code' : 'El código de producto ingresado no existe'}}, status = 400)
