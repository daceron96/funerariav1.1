$("#supplier-form").on('submit', function(e){
    e.preventDefault();

})

function create_supplier(){
	$.ajax({
		url : $("#supplier-form").attr('action'),
		type : $("#supplier-form").attr('method'),
		data : $("#supplier-form").serializeArray(),
		dataType: 'json',
		success: (response) =>{
			$('.table-active').removeClass('table-active');
			let item = "<tr class='table-active text-muted' id='tr-"+response.id+"' onclick='supplier_detail("+response.id+")'>"
				+ "<th id='td-state-"+response.id+"'><i class='bi bi-check-circle-fill text-success'></i>"
                + "<th>" + response.identifier + "</th>"
				+ "<td id='td-name-"+response.id +"'>" + response.name + "</td>"
				+ "<td id='td-phone-"+response.id +"'>" + response.phone + "</td>"
				+ "<td class='text-danger fw-semibold'><i class='bi bi-patch-check-fill'></i> 0</td>"
				+ "<td class='text-success fw-semibold'><i class='bi bi-patch-exclamation-fill'></i> 0</td>"
				+ "<td class='text-success fw-semibold' ><i class='bi bi-patch-exclamation-fill'></i> 0</td>"
				
			+"<tr>"
			$('#supplier-table-list').prepend(item)
			reset_form("supplier-form","proveedor","create_supplier")
			success("Registro de nuevo proveedor","El nuevo proveedor ha sido registrado exitosamente")
		},
		error: (response) =>{
			message_error(response.responseJSON.error)
		}
	})
}
function supplier_detail(id){
    $.ajax({
        url : '/supplier/detail/'+id,
        type : 'GET',
        success: (response) =>{
            $("#supplier-detail-modal").modal('show')
            $('#supplier-name').empty().append("<i class='bi bi-person-circle fs-5 '></i> " + response.name)
            $('#supplier-identifier').empty().append("<i class='bi bi-postcard-fill fs-5 '></i> " + response.identifier)
            if(response.phone !== null){
                $('#supplier-phone').empty().append("<i class='bi bi-phone-vibrate-fill fs-5'></i> " + response.phone)
            }else{
                $('#supplier-phone').empty().append("<i class='bi bi-phone-vibrate-fill fs-5'></i>  No registrado")
            }
            $('#supplier-list-modal').empty()
            
            response.product_list.forEach(detail => {
                let item = `<tr>
                    <th> ${detail.code} </th>
                    <td> ${detail.name} </th>`

                if(detail.stock_cellar > 10){
                    item +=(`<td class='text-success fw-semibold'><i class='bi bi-patch-check-fill'></i> ${detail.stock_cellar} </td>`)
                }else if(detail.stock_cellar > 0){
                    item +=(`<td class='text-warning fw-semibold'><i class='bi bi-patch-exclamation-fill'></i>   ${detail.stock_cellar}  </td>`)
                }else{
                    item +=(`<td class='text-danger fw-semibold'><i class='bi bi-patch-exclamation-fill'></i> ${detail.stock_cellar} </td>`)
                }

                if(detail.stock_wait > 0){
                    item +=(`<td class='text-warning fw-semibold'><i class='bi bi-patch-exclamation-fill'></i>   ${detail.stock_wait}  </td>`)
                }else{
                    item +=(`<td class='text-success fw-semibold'><i class='bi bi-patch-check-fill'></i>   ${detail.stock_wait}  </td>`)
                }
                if(detail.stock_loan > 0){
                    item +=(`<td class='text-warning fw-semibold'><i class='bi bi-patch-exclamation-fill'></i> ${detail.stock_loan}  </td>`)
                }else{
                    item +=(`<td class='text-success fw-semibold'><i class='bi bi-patch-check-fill'></i> ${detail.stock_loan}  </td>`)
                }
                
                item +=(`</tr>`)
                $('#supplier-list-modal').append(item)
            });
            $('#btn-update-supplier').attr("onClick", `supplier_get_detail(${id})`)
            $('#btn-state-suppllier').remove()
            $('#btn-detail-modal').append(btn_state(response.state,response.id))
            

        }
    })
}

function supplier_get_detail(id){

    $.ajax({
        url : `/supplier/update/${id}`,
        type : 'GET', 
        success :(response) =>{
            $('#title-modal-supplier-form').text("Actualizar datos de proveedor")
            $('#identifier').val(response.identifier)
            $('#name').val(response.name)
            $('#phone').val(response.phone)
            $('#btn-update-supplier').attr("onClick", `supplier_get_detail(${id})`)
            $('#btn-save').attr("onClick", `update_supplier(${id})`)
            $("#supplier-detail-modal").modal('hide')
            $('#supplier-form-modal').modal('show')
        }
    })
}

function update_supplier(id){
	$.ajax({
		url : `/supplier/update/${id}/`,
		type : "POST",
		data : $("#supplier-form").serializeArray(),
		dataType: 'json',
		success : (response) =>{
			$(`#td-name-${id}`).text(response.name)
			$(`#td-phone-${id}`).text(response.phone)
			$(`.table-active`).removeClass('table-active')
			$(`#tr-${id}`).addClass('table-active')
            $('#supplier-form-modal').modal('hide')
			reset_form("supplier-form","proveedor","create_supplier")
			success("Actualizacion de proveedor","La actualizacion de información del proveedor ha sido exitosa")

		}
	})
}

function change_state_supplier(id){
    $.ajax({
        url : `/supplier/change/${id}/`,
        method : 'POST',
        data : {csrfmiddlewaretoken : getCSRFToken()},

        success : (response) =>{
            $(`#td-state-${response.id}`).empty().append(
                response.state ? '<i class="bi bi-check-circle-fill text-success"></i>' : '<i class="bi bi-x-circle-fill text-danger"></i>'
            )
            $("#supplier-detail-modal").modal('hide')
			$(`.table-active`).removeClass('table-active')
			$(`#tr-${id}`).addClass('table-active')
			success("Cambio de estado","El estado del proveedor ha sido actualizado exitosamente")

        }
    })
}