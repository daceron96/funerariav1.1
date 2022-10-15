const tr_table_add = (element) => {
	return `<tr id='tr-add-${element.id}'>
		<th>${element.code}</th>
		<td>${element.name}</td>
		<td id='quantity-${element.id}'>1</td>
		<td>
			<button type='button' class='btn btn-danger' id='btn-delete-${element.id}' onClick='delete_item(${element.id})'>
				<i class='bi bi-trash3'></i>
			</button>
		</td>
	</tr>`
}

const tr_table_detail = (element) => {
	return `<tr>
		<th>${element.product_code} </th>
		<td>${element.product_name}</td>		
		<td>${element.product_category}</td>		
		<td>${element.quantity}</td>		
	</tr>`
}

const tr_table_list = (element) => {
	return `<tr id='tr-list-${element.id}' class='text-muted table-active' onClick='output_detail(${element.id})'> 
		<th>${element.reference} </th>
		<td>${element.output_type} </td>
		<td>${element.name_client} </td>
		<td>${element.quantity} </td>
		<td>${element.created_date} </td>
	</tr>`
}