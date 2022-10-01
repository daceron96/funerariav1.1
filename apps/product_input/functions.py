from PIL import Image, ImageDraw, ImageFont
import qrcode
from django.http import JsonResponse
from apps.product.models import Product
from apps.supplier.models import Supplier
from .models import InputDetail, ProductInput


#TODO Falta por implementar no funciona T.T 
def autocomplete_product(request):
	print(request)
	term = request.GET.get('term')
	query_name = Product.objects.filter(name__icontains = term)
	query_code = Product.objects.filter(code__icontains = term)
	query = {}
	list = ['gola',]
	for product in query_code:
		query[product.code] = product.name

	for product in query_name:
		query[product.code] = product.name

	return JsonResponse(list, safe=False)

def validate_data(data):
	errors  = {}
	supplier = None
	try:
		supplier = Supplier.objects.get(identifier = data['supplier'])
	except:
		errors['supplier'] = 'El proveedor no existe'
	
	try:
		ProductInput.objects.get(reference = data['reference'])
		errors['reference'] = 'Ya existe una entrada registrada con este numero de referencia'
	except:
		if(len(data['reference'].strip()) == 0):
			errors['reference'] = 'Campo no valido'

	return supplier, errors

def create_qr_code(pk):
	
	product_input = ProductInput.objects.get(id = pk)
	detail_list = InputDetail.objects.filter(product_input = product_input)
	img_final = Image.new('RGB', (659 * product_input.quantity,340),'white')
	count = 0

	for detail in detail_list:
		product = Product.objects.get(id = detail.product.id)
		initial_consecutive = product.consecutive
		consecutive_list = []
		for index in range(detail.quantity):
			initial_consecutive += 1
			code = f'{product.code}-{initial_consecutive}'
			data = f'{code}|{product_input.supplier.identifier}'
			img_qr = qrcode.make(data)
			logo = Image.open("media/logo.jpeg")
			icon = Image.open("media/icono.png")
			img_qr.size
			logo.size
			img_qr_size = img_qr.resize((310,310))
			logo_size = logo.resize((328,310))
			img_aux = Image.new('RGB',(659,340), 'white')
			img_aux.paste(img_qr_size,(0,0))
			img_aux.paste(logo_size,(310,0))
			if((index+1) != detail.quantity):
				img_aux.paste(icon,(638,0))	

			string = f'{code} | {product.category.name} | {product_input.reference}'	
			draw = ImageDraw.Draw(img_aux)
			font = ImageFont.truetype("arial.ttf", 25)
			draw.text((20, 290), string, font=font, fill="black")
			img_final.paste(img_aux,(count,0))
			count += 659
			consecutive_list.append(data)
			detail.code_list = consecutive_list
			detail.save()
		product.consecutive += detail.quantity
		product.save()
		url = 'media/codigos-qr/'+product_input.reference + '.png'
		img_final.save(url)
		product_input.created_qr = True
		product_input.image_qr = url
		product_input.save()
			