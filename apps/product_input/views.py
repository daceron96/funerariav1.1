from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import JsonResponse
import json
from apps.product.models import Product, ProductDetail
from .functions import validate_data,create_qr_code
from .models import ProductInput, InputDetail


class ProductInputListView(ListView):
    model = ProductInput
    template_name = 'input/input_list.html'


class ProductInputCreateView(CreateView):
    model = ProductInput

    def post(self, *args, **kwargs):
        data = json.loads(self.request.POST['form'])
        list = json.loads(self.request.POST['list'])
        supplier, errors = validate_data(data)
        if (len(list) == 0):
            errors['product'] = "Debes ingresar almenos un producto en la lista"
        if (supplier and not errors):
            quantity = 0
            product_input = self.model.objects.create(
                reference=data['reference'],
                supplier=supplier
            )
            for item in list:
                product = Product.objects.get(id=item['id'])
                InputDetail.objects.create(
                    product=product,
                    product_input=product_input,
                    quantity=item['quantity']
                )
                # verifica si existe un detalle ya creado y suma la cantidad si no crea un nuevo detalle
                try:
                    detail = ProductDetail.objects.get(
                        product=product, supplier=supplier)
                    detail.stock_wait += item['quantity']
                    detail.save()
                except:
                    ProductDetail.objects.create(
                        product=product,
                        supplier=supplier,
                        stock_wait=item['quantity']
                    )
                quantity += item['quantity']

            product_input.quantity = quantity
            product_input.save()

            return JsonResponse({
                'id': product_input.id,
                'reference': product_input.reference,
                'supplier': supplier.name,
                'quantity': product_input.quantity,
                'created': product_input.created_date
            }, status=200)
        return JsonResponse({'error': errors}, status=400)


class ProductInputDetailView(DetailView):
    model = ProductInput

    def get(self, *args, **kwargs):
        product_list = []
        query = InputDetail.objects.filter(product_input=self.get_object())
        for detail in query:
            data = {
                'id': detail.product.id,
                'code': detail.product.code,
                'name': detail.product.name,
                'category': detail.product.category.name,
                'quantity': detail.quantity,
            }
            product_list.append(data)

        return JsonResponse({
            'id': self.get_object().id,
            'in_wait': self.get_object().in_wait,
            'reference': self.get_object().reference,
            'created_qr' : self.get_object().created_qr,
            'supplier': f'{self.get_object().supplier.identifier} - {self.get_object().supplier.name} ',
            'description': self.get_object().description,
            'created_date': self.get_object().created_date,
            'product_list': product_list
        })


class ProductInputUpdateView(UpdateView):
    model = ProductInput

    def post(self,*args, **kwargs):

        product_input = self.get_object()
        detail_list = InputDetail.objects.filter(product_input = product_input )
        product_list = json.loads(self.request.POST['list'])
        detail_delete = []
        errors = {}
        if (len(product_list) == 0):
            errors['product'] = "Debes ingresar almenos un producto en la lista"
            return JsonResponse({'error': errors}, status=400)
        for detail in detail_list:
            delete = True
            for index in range(len(product_list)):
                if(detail.product.id == product_list[index]['id']):
                    
                    if(detail.quantity != product_list[index]['quantity']):
                        product_input.quantity -= detail.quantity
                        product_detail = ProductDetail.objects.get(product=detail.product, supplier=product_input.supplier)
                        product_detail.stock_wait -= detail.quantity
                        detail.quantity = product_list[index]['quantity']
                        product_detail.stock_wait += detail.quantity
                        product_input.quantity += detail.quantity
                        product_detail.save()
                        detail.save()
                        product_input.save()
                    del product_list[index]
                    delete = False
                    break
            if(delete):
                detail_delete.append(detail)
        
        for delete in detail_delete:
            product_input.quantity -= delete.quantity
            product_detail = ProductDetail.objects.get(product=delete.product, supplier=product_input.supplier)
            product_detail.stock_wait -= delete.quantity
            delete.delete()
            product_input.save()
            product_detail.save()

        for add in product_list:
            product = Product.objects.get(pk = add['id'])
            InputDetail.objects.create(
                    product=product,
                    product_input=product_input,
                    quantity=add['quantity']
                )
            try:
                detail = ProductDetail.objects.get(
                    product=product, supplier=product_input.supplier)
                detail.stock_wait += add['quantity']
                detail.save()
            except:
                ProductDetail.objects.create(
                    product=product,
                    supplier=product_input.supplier,
                    stock_wait=add['quantity']
                    )
            product_input.quantity += add['quantity']
            product_input.save()

        
        return JsonResponse({
            'id': product_input.id,
            'quantity' : product_input.quantity
        }, status=200)

class ProductInputDepositView(View):
    #TODO revisar esta funcion     
    def get(self,*args, **kwargs):
        pk = self.kwargs['pk']
        product_input = ProductInput.objects.get(id = pk)
        if(not product_input.created_qr):
            create_qr_code(pk)
        product_input = ProductInput.objects.get(id = pk)
        product_list = []
        query = InputDetail.objects.filter(product_input=product_input)
        for detail in query:
            data = {
                'id': detail.product.id,
                'code': detail.product.code,
                'name': detail.product.name,
                'category': detail.product.category.name,
                'quantity': detail.quantity,
                'code_list' : eval(detail.code_list)
            }
            product_list.append(data)
        return JsonResponse({
            'reference' : product_input.reference,
            'supplier' : f'{product_input.supplier.identifier} - {product_input.supplier.name}',
            'url' : product_input.image_qr,
            'data':product_list})
    # TODO falta capturar la lista de codigos y validarlos 
    def post(self, *args, **kwargs):
        pk = self.kwargs['pk']
        product_input = ProductInput.objects.get(id = pk)
        details = InputDetail.objects.filter(product_input=product_input)

        for detail in details:
            product_detail = ProductDetail.objects.get(supplier = product_input.supplier, product = detail.product)
            try:
                code_list = eval(product_detail.code_list)
                code_list.append(eval(detail.code_list))
            except:
                code_list = eval(detail.code_list)
            
            product_detail.stock_wait -= detail.quantity
            product_detail.stock_cellar += detail.quantity
            product_detail.code_list = code_list
            product_detail.save()
        product_input.in_wait = False
        product_input.save()

        return JsonResponse({'id':product_input.id})