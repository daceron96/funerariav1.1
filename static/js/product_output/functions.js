$(document).ready(function () {
	$("#link-output").addClass("active");
});

function reset_output(){
	
	reset_form(`output-form`,'entrada','create_output')
	$('#output_product_list').empty()
	$('#code').removeClass('is-valid')
	product_list = []
	$('#alert-list').addClass('visually-hidden')
}

const item = (item) => {
	return {
		id: item.id,
		code: item.code,
		name: item.name,
		code_list : [item.code_list],
	};
};

const validate_code = (code) => {

	index = code.indexOf('-')
	product_code = code.substring(0,index)
	let flag = false
	product_list.forEach(element => {
		if(element.code === product_code){
			flag = element.code_list.includes(code)
		}
	})
	if(flag){
		message_error({code:'El codigo ya ha sido ingresado'})
	}

	return flag
}

const verify_product = (response_code) => {
	index = response_code.indexOf('-')
	product_code = response_code.substring(0,index)
	let flag = false
	product_list.forEach(element => {
		if(element.code == product_code){
			element.code_list.push(response_code)
			$('#code').addClass('is-valid').val('').focus()
			$(`#quantity-${element.id}`).text(`${element.code_list.length}`)
			flag = true
		}
	})
	return flag
}

function delete_item(id){
	product_list.forEach((element,index) => {
		if(element.id === id){
			product_list.splice(index,1)
			$(`#tr-add-${element.id}`).remove()
		}
	})
}