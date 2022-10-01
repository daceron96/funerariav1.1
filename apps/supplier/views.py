from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.http import JsonResponse
from django.views import View
from apps.product.models import ProductDetail

from apps.supplier.models import Supplier
from apps.supplier.forms import SupplierForm

class SupplierListView(ListView):
	model = Supplier
	template_name = 'supplier/supplier_list.html'
	


class SupplierDetailView(DetailView):
	model = Supplier
	
	def get(self,request, *args, **kwargs):

		product_list = []
		query = ProductDetail.objects.filter(supplier = self.get_object())
		for detail in query:
			#TODO esta sumando todas las cantidades hay que mejorar el filtro :V
			data = {
				"code" : detail.product.code,
				"name" : detail.product.name,
				"stock_cellar" : detail.product.stock_cellar['stock_cellar__sum'],
				"stock_wait" : detail.product.stock_wait['stock_wait__sum'],
				"stock_loan" : detail.product.stock_loan['stock_loan__sum'],
			}
			product_list.append(data)

		response = JsonResponse({
				'id':self.get_object().id,
				'identifier':self.get_object().identifier,
				'name':self.get_object().name,
				'phone':self.get_object().phone,
				'state': self.get_object().state,
				'product_list' : product_list
			}, status = 200)
		return response

class SupplierCreateView(CreateView):
	model = Supplier
	form_class = SupplierForm
	def post(self,request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			form.save()
			response = JsonResponse({
				'id':form.instance.id,
				'identifier':form.instance.identifier,
				'name':form.instance.name,
				'phone':form.instance.phone,
			}, status = 200)
			return response
		return JsonResponse({'error':form.errors}, status = 400)

class SupplierUpdateView(UpdateView):
	model = Supplier
	form_class = SupplierForm

	def get(self,*args, **kwargs):
		return JsonResponse({
			"name": self.get_object().name,
			"identifier": self.get_object().identifier,
			"phone": self.get_object().phone,
		}, status = 200)

	def post(self, *args, **kwargs):
		form = self.form_class(self.request.POST, instance=self.get_object())
		if form.is_valid():
			form.instance.identifier = self.get_object().identifier
			form.save()
			return JsonResponse({
				"id": form.instance.id,
				"name": form.instance.name,
				"identifier": form.instance.identifier,
				"phone": form.instance.phone,
			}, status = 200)
		return JsonResponse({'error': form.errors},status = 400)
	
class SupplierChangeState(View):

	def post(self, *args, **kwargs):
		pk = self.kwargs['pk']
		
		try:
			supplier = Supplier.objects.get(pk = pk)
			supplier.state = False if supplier.state else True
			supplier.save()
			return JsonResponse({'id':pk, 'state':supplier.state},status = 200)
		except:
			return JsonResponse({'error':"El proveedor no existe"},status = 400 )
