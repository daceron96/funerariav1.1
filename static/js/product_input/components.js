

const tr_table_add = (element) => {
	return `<tr id='tr-add-${element.id}'>
		<th>${element.code}</th>
		<td>${element.name}</td>
		<td id='quantity-${element.id}'>${element.quantity}</td>
		<td>
			<button type='button' class='btn btn-warning text-white' id='btn-subtract-${element.id}' onClick='subtract_quantity(${element.id})'>
				<i class='bi bi-dash'></i>
			</button>
			<button type='button' class='btn btn-danger' id='btn-delete-${element.id}' onClick='delete_item(${element.id})'>
				<i class='bi bi-trash3'></i>
			</button>
			<button type='button' class='btn btn-success' id='btn-add-${element.id}' onClick='add_quantity(${element.id})'>
				<i class='bi bi-plus'></i>
			</button>
		</td>
	</tr>`
}



const tr_table_deposit = (element) =>{
	return `<tr id='tr-deposit-${element.id}'>
		<td class='text-warning fw-semibold' id='deposit-state-${element.id}'><i class="bi bi-patch-exclamation-fill"></i>
		<th>${element.code} </th>
		<td>${element.name} </td>
		<td id='quantity-deposit-${element.id}'> ${element.quantity} </td>
		<td id='deposit-${element.id}'> 0 </td>
	</tr>`
}

const tr_list = (element) => {
    return `<tr id='tr-list-${element.id}' class='table-active text-muted' onClick='input_detail(${element.id})'> 
        <td id="td-state-${element.id}"><i class="bi bi-patch-exclamation-fill text-warning"></i></td>
        <th>${element.reference} </th>
        <td>${element.supplier} </td>
        <td id='quantity-${element.id}'>${element.quantity} </td>
        <td>${element.created} </td>
    </tr>`
}

const tr_detail_list = (element) => {
	return `<tr class='text-muted'>
		<th>${element.code} </th>
		<td>${element.name} </td>
		<td>${element.category} </td>
		<td>${element.quantity} </td>
	</tr>
	`
}

const btn_deposit = (id) =>{
	return `<button type="button" class="btn btn-warning text-white" id='btn-deposit' onClick='input_get_detail_deposit(${id})'>
		<i class="bi bi-boxes   "></i> Ingresar
	</button>`
}

const btn_update_deposit = (id) =>{
	return `<button type="button" class="btn btn-primary" id='btn-update-input' onClick='input_get_detail(${id})'>
		<i class="bi bi-boxes   "></i> Modificar
	</button>`
}
