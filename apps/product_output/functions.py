from django.http import JsonResponse
from .models import ProductOutput
from apps.core.functions import parse_date

def serialize_data(query):
		output_list = []
		for output in query:
				data = {
						'id' : output.id,
            'reference' : output.reference,
            'output_type' : output.output_type.name,
            'name_client' : output.name_client,
            'quantity' : output.quantity,
            'created_date' : parse_date(output.created_date)
						
				}
				output_list.append(data)
		return output_list


def filter_output_by_type(request):
	
	if request.GET:
		pk = request.GET.get('pk')
		if(pk != '-1'):
			query = ProductOutput.objects.filter(output_type = pk)
		else:
			query = ProductOutput.objects.all()
		output_list = serialize_data(query)
		return JsonResponse({'data': output_list}, status=200)
