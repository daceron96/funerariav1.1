from itertools import product
import json
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import ProductLoan, LoanType, LoanDetail
from apps.product.models import ProductDetail
from .forms import ProductLoanForm
from apps.core.functions import parse_date
from apps.product.functions import validate_list

class ProductLoanListView(ListView):
  model = ProductLoan
  template_name = 'loan/loan_list.html'

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    context['loan_type'] = LoanType.objects.all().values('id','name')
    return context

class ProductLoanCreateview(CreateView):
  model = ProductLoan
  form_class: ProductLoanForm

  def post(self, *args, **kwargs):
    form = json.loads(self.request.POST['form'])
    list = json.loads(self.request.POST['list'])
    if(len(list) == 0):
      return  JsonResponse({'error': {'product': "Ingresa almenos un producto en la lista"}}, status=400)
    else:
      try:
        for product in list:
          for code in product['code_list']:
            code.index('-')
            code.index('|')
      except:
        return JsonResponse({'error': {'product': "Formato de codigo incorrecto"}}, status=400)

    form = ProductLoanForm(form)
    if(form.is_valid()):
      error, index_list = validate_list(list)
      if(len(error) == 0):
        form.save()
        for key in index_list.keys():
          detail = ProductDetail.objects.get(id = key)
          code_list = eval(detail.code_list)
          product = detail.product
          for code in index_list[key]:
            code_list.remove(code)
          
          if len(code_list) == 0:
            detail.code_list = ''
          else:
            detail.code_list = code_list
          detail.stock_cellar -= len(index_list[key])
          detail.stock_loan += len(index_list[key])
          
          LoanDetail.objects.create(
            product = product,
            quantity = len(index_list[key]),
            code_list = str(index_list[key]),
            product_loan = ProductLoan.objects.get(id = form.instance.id)
          )
          detail.save()
          form.instance.quantity += len(index_list[key])
        
        form.save()
        return JsonResponse({
          'id' : form.instance.id,
          'reference' : form.instance.reference,
          'loan_type' : form.instance.loan_type.name,
          'name_client' : form.instance.name_client,
          'quantity' : form.instance.quantity,
          'created_date' : parse_date(form.instance.created_date)
        })
    return JsonResponse({'error': form.errors}, status=400)

class ProductLoanDetailView(DetailView):
  model = ProductLoan

  def get(self, *args, **kwargs):
    loan_list = []
    query = LoanDetail.objects.filter(product_loan = self.get_object())
    for detail in query:
      data = {
        'product_code' : detail.product.code,
        'product_name' : detail.product.name,
        'product_category' : detail.product.category.name,
        'quantity' : detail.quantity
      }
      loan_list.append(data)
    
    return JsonResponse({
      'reference' : self.get_object().reference,
      'loan_type' : self.get_object().loan_type.name,
      'identifier' : self.get_object().identifier,
      'name_client' : self.get_object().name_client,
      'description' : self.get_object().description,
      'quantity' : self.get_object().quantity,
      'created_date' : parse_date(self.get_object().created_date),
      'loan_list' : loan_list
    }, status = 200)