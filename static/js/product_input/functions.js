$(document).ready(function () {
	$("#link-input").addClass("active");
});
$("#deposit-form").on('submit', function(evt){
    evt.preventDefault(); 
	validate_code_list()

});

function product_autocomplete() {
	console.log('as')
	$("#code").autocomplete({
        source: '/input/autocomplete-product/',
        autoFocus: true
    });
}

const item = (item, quantity) => {
	return {
		id: item.id,
		code: item.code,
		name: item.name,
		quantity: parseInt(quantity),
	};
};


function search_product(code,quantity){
	let bandera = true
	product_list.forEach(element => {
		if(element.code === code){
			console.log('holis')
			$('#code').removeClass('is-invalid').val('').focus()
			$('#quantity').removeClass('is-invalid').val('')
			element.quantity += parseInt(quantity)
			quantity_update(element.id, element.quantity)
			bandera = false
			
		}
	});
	return bandera
}

function validate_code(code,quantity){
	error = {}
	if(code.length == 0){
		error['code'] = 'Debes ingresar un codigo'
	}else{
		$('#code').removeClass('is-invalid')
	}
	if(quantity.length == 0 || quantity < 1){
		error['quantity'] = 'Cantidad no valida'
	}else{
		$('#quantity').removeClass('is-invalid')
	}
	if($.isEmptyObject(error)){
		return true
	}
	message_error(error)
	return false
}


function quantity_update(id,quantity){
	$(`#quantity-${id}`).text(quantity)
}

function subtract_quantity(id){
	product_list.forEach(element => {
		if(element.id == id){
			element.quantity --;
			quantity_update(id,element.quantity)
			if(element.quantity == 1){
				$(`#btn-subtract-${element.id}`).attr('disabled','true')
			}
		}
	})
}
function add_quantity(id){
	product_list.forEach(element => {
		if(element.id == id){
			element.quantity ++;
			quantity_update(id,element.quantity)
			$(`#btn-subtract-${element.id}`).removeAttr('disabled')

		}
	})
}

function delete_item(id){
	product_list.forEach((element,index) => {
		if(element.id === id){
			product_list.splice(index,1)
			$(`#tr-add-${element.id}`).remove()
		}
	})
}


function reset_input(name='input'){
	reset_form(`${name}-form`,'entrada','create_input')
	$('#alert-list').addClass('visually-hidden')
	$(`#${name}_product_list`).empty()
	$(`#input_deposit_list`).empty()
	product_list = []
}


const get_subcode = (code) =>{
	let index = code.indexOf('-')
	code = code.substring(0,index)
	return code

}


function validate_code_list(){
	let code = $('#code-deposit').val().trim()
	let subcode = get_subcode(code)
	$('#code-deposit').removeClass('is-invalid is-valid')
	
	let index = product_list.findIndex(element => element.code == subcode)
	if(index != -1){
		var flag = false 
		product_list[index].code_list.forEach((element,subindex) => {
			if(element === code){
				product_list[index].quantity --
				product_list[index].deposit ++
				$(`#quantity-deposit-${product_list[index].id}`).text(product_list[index].quantity)
				$(`#deposit-${product_list[index].id}`).text(product_list[index].deposit)
				flag = true
				product_list[index].code_list.splice(subindex,1)
			}

		})
		if(product_list[index].quantity == 0){
			$(`#deposit-state-${product_list[index].id}`).empty().append(
				`<i class="bi bi-patch-check-fill text-success"></i>`
			)
			product_list.splice(index,1)

		}
		if(product_list.length ==0){
			$('#btn-save-deposit').removeClass('disabled')
		}
		if(flag){
			$('#code-deposit').addClass('is-valid')
			$('#valid-code-deposit').text('Codigo registrado')
			$('#code-deposit').val('').focus()
		}else{
			$('#code-deposit').addClass('is-invalid')
			$('#invalid-code-deposit').text('Codigo invalido o ya ha sido registrado')
		}
	}else{
		$('#code-deposit').addClass('is-invalid')
		$('#invalid-code-deposit').text('Codigo invalido')
	}
	

}