from django.http import JsonResponse
from .models import ProductLoan
from apps.core.functions import parse_date

def serialize_data(query):
		loan_list = []
		for loan in query:
				data = {
						'id' : loan.id,
            'reference' : loan.reference,
            'loan_type' : loan.loan_type.name,
            'name_client' : loan.name_client,
            'quantity' : loan.quantity,
            'created_date' : parse_date(loan.created_date)
						
				}
				loan_list.append(data)
		return loan_list


def filter_loan_by_type(request):
	
	if request.GET:
		pk = request.GET.get('pk')
		if(pk != '-1'):
			query = ProductLoan.objects.filter(loan_type = pk)
		else:
			query = ProductLoan.objects.all()
		loan = serialize_data(query)
		return JsonResponse({'data': loan}, status=200)
