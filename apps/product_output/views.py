import json
from humanize import intcomma
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import View

from .forms import ProductOutputForm
from .models import ProductOutput, OutputType, OutputDetail
from apps.core.functions import parse_date
from apps.product.models import ProductDetail
from apps.product.functions import validate_list



class ProductOutputListView(ListView):
    model = ProductOutput
    template_name = 'output/output_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["output_type"] = OutputType.objects.filter().values('id','name')
        return context


class ProductOutputDetailView(DetailView):
    model = ProductOutput

    def get(self, *args, **kwargs):
        output_list = []
        query = OutputDetail.objects.filter(product_output = self.get_object())
        for detail in query:
            data = {
                'product_code' : detail.product.code,
                'product_name' : detail.product.name,
                'product_category' : detail.product.category.name,
                'quantity' : detail.quantity
            }
            output_list.append(data)
        return JsonResponse({
            'reference' : self.get_object().reference,
            'output_type' : self.get_object().output_type.name,
            'identifier' : self.get_object().identifier,
            'name_client' : self.get_object().name_client,
            'description' : self.get_object().description,
            'price_total' : intcomma(self.get_object().price_total),
            'quantity' : self.get_object().quantity,
            'invoice_number' : self.get_object().invoice_number,
            'created_date' : parse_date(self.get_object().created_date),
            'output_list' : output_list
        }, status = 200)


class ProductOutputCreateView(CreateView):
    model = ProductOutput
    form_class = ProductOutputForm

    def post(self, *args, **kwargs):
        form = json.loads(self.request.POST['form'])
        list = json.loads(self.request.POST['list'])
        if (len(list) == 0):
            return JsonResponse({'error': {'product': "Ingresa almenos un producto en la lista"}}, status=400)
        else:
            try:
                for product in list:
                    for code in product['code_list']:
                        code.index('-')
                        code.index('|')
            except:
                return JsonResponse({'error': {'product': "Formato de codigo incorrecto"}}, status=400)
                
        form = ProductOutputForm(form)
        if (form.is_valid()):
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
                    
                    OutputDetail.objects.create(
                        product = product,
                        quantity = len(index_list[key]),
                        code_list = str(index_list[key]),
                        product_output = ProductOutput.objects.get(id = form.instance.id)
                    )
                    detail.save()
                    form.instance.quantity += len(index_list[key])
                form.save()
                return JsonResponse({
                    'id' : form.instance.id,
                    'reference' : form.instance.reference,
                    'output_type' : form.instance.output_type.name,
                    'name_client' : form.instance.name_client,
                    'quantity' : form.instance.quantity,
                    'created_date' : form.instance.created_date

                }, status = 201)

        return JsonResponse({'error': form.errors}, status=400)


