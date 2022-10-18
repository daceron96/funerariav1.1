function mayus(e) {
	e.value = e.value.toUpperCase();
}
$('#product-form').on('submit', function(e){
	e.preventDefault();
})
function create_product(){
	
	$.ajax({
		url : $('#product-form').attr('action'),
		type: $('#product-form').attr('method'),
		data : $('#product-form').serializeArray(),
		dataType: 'json',

		success: function(response){
			$('.table-active').removeClass('table-active');
			let item = `
				<tr class='table-active text-muted' id='tr-${response.id}' onClick=product_detail(${response.id})>
				<td id='td-state-${response.id}'><i class='bi bi-check-circle-fill text-success'></i></td>
				<th> ${response.code} </th>
				<td id='td-name-${response.id}'> ${response.name} </td>
				<td id='td-category-${response.id}'> ${response.category} </td>`
				item += td_style_danger(0)
				item += td_style_success(0)
				item += td_style_success(0)
				item +=`</tr>`
			$('#product-table-list').prepend(item)
			reset_form("product-form","producto","create_product")
			success("Registro de nuevo producto","El nuevo producto ha sido registrado exitosamente")
			$('#success-modal').modal('show')
		},
		error: function (response) {
			message_error(response.responseJSON.error)
		}
	})
}

function product_detail(id_product){

	$.ajax({
		url : `/product/detail/${id_product}/`,
		type : "GET",
		success : (response) =>{
			//date of product
			$('#title-modal').empty().append(`Detalle de producto ${response.code} - ${response.name}`)
			$('#code-modal').empty().append(`<i class="bi bi-journal-medical fs-5"></i> Codigo: ${response.code}`)
			$('#name-modal').empty().append(`<i class="bi bi-journal-minus  fs-5"></i> Nombre: ${response.name}`)
			$('#category-modal').empty().append(`<i class="bi bi-card-checklist fs-5"></i> Categoria: ${response.category}`)
			$('#created-modal').empty().append(`<i class="bi bi-calendar-date fs-5"></i> Fecha de registro: ${response.created_date}`)
			response.description.length  == 0 ?
			$('#description-modal').empty().append(`<i class="bi bi-chat-left-text fs-5 "></i> Descripcion: Sin descripcion`)
			:
			$('#description-modal').empty().append(`<i class="bi bi-chat-left-text fs-5 "></i> Descripcion: ${response.description}`)
			$('#product-detail-modal').modal('show')

			// date of table supplier
			$('#product-detail-list').empty()
			response.supplier_list.forEach(supplier => {
				item = `<tr>
					<th>${supplier.identifier}</th>
					<td>${supplier.name}</td>`
					if(supplier.stock_cellar > 10){
						item += td_style_success(supplier.stock_cellar)
					}else if(supplier.stock_cellar > 0){
						item += td_style_warning(supplier.stock_cellar)
					}else{
						item += td_style_danger(supplier.stock_cellar)
					}
	
					if(supplier.stock_wait > 0){
						item += td_style_warning(supplier.stock_wait)
					}else{
						item += td_style_success(supplier.stock_wait)
					}
					if(supplier.stock_loan > 0){
						item += td_style_warning(supplier.stock_loan)
					}else{
						item += td_style_success(supplier.stock_loan)
					}
				item +=`</tr>`

				$('#product-detail-list').append(item)
			});
            $('#btn-update-product').attr("onClick", `product_get_detail(${response.id})`)
			$('#btn-state-suppllier').remove()
            $('#btn-detail-modal').append(btn_state(response.state,response.id))
			
		}
	})

}

function product_get_detail(id_product){
	
	$.ajax({
		url : `/product/update/${id_product}/`,
		type : 'GET',

		success : (response) =>{
			$('#code').val(response.code)
			$('#name').val(response.name)
			$('#category').val(response.category)
			$('#description').val(response.description)
            $('#btn-save').attr("onClick", `update_product(${response.id})`)
			$('#product-detail-modal').modal('hide')
			$("#product-form-modal").modal('show')
		}
	})

}

function update_product(id_product){
	
	$.ajax({
		url : `/product/update/${id_product}/`,
		type : "POST",
		data : $('#product-form').serializeArray(),
		success : (response) => {
			$(`#td-name-${response.id}`).text(response.name)
			$(`#td-category-${response.id}`).text(response.category)
			$('.table-active').removeClass('table-active')
			$(`#tr-${response.id}`).addClass('table-active')
			reset_form('product-form','producto','create_product')
			success("Actualizacion de producto","La actualizacion de informacion del producto ha sido exitosa")

		}
	})

}

function change_state_product(id_product){

	$.ajax({
		url : `/product/change/${id_product}/`,
		type: "POST",
		data : {csrfmiddlewaretoken : getCSRFToken()},

		success : (response) => {
			$(`#td-state-${response.id}`).empty().append(
                response.state ? '<i class="bi bi-check-circle-fill text-success"></i>' : '<i class="bi bi-x-circle-fill text-danger"></i>'
            )

            $("#product-detail-modal").modal('hide')
			$(`.table-active`).removeClass('table-active')
			$(`#tr-${response.id}`).addClass('table-active')
			success("Cambio de estado","El estado del producto ha sido actualizado exitosamente")
		}

	})

}

function search_product(){

	$.ajax({
		url : '/product/filter/name/',
		method : 'GET',
		data :{'term':  $('#input_search').val().trim()},

		success : (response) =>{
			$('#product-table-list').empty()

			response.data.forEach( element => {
				$('#product-table-list').prepend(tr_table_list(element))
			})
		}
	})
}

function filter_product(){

	$.ajax({
		url : '/product/filter/category/',
		method : 'GET',
		data : {pk : $('#select_category').val()},
		success : (response) =>{
			$('#product-table-list').empty()
			response.data.forEach(data => {
				$('#product-table-list').prepend(tr_table_list(data))
			})
		}
	})

}