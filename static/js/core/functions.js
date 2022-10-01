function message_error(obj){
    $('.is-invalid').removeClass('is-invalid')
    $.each(obj, function(key, value){
        $('#'+key).addClass('is-invalid');
        $('#invalid-'+key).empty().append(value);
    })
}

function reset_form(form_name,title,name_fun){
	$("#"+form_name)[0].reset();
    $('.is-invalid').removeClass('is-invalid');
	$("#"+form_name+"-modal").modal('hide')
    $(`#title-modal-${form_name}`).text(`Registrar nuevo ${title}`)
    $('#title-modal-form').text("Actualizar datos de proveedor")
    $("#btn-save").attr("onClick", `${name_fun}()`)
}

function getCSRFToken() {
	let cookieValue = null;
	if (document.cookie && document.cookie != '') {
		let cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			let cookie = jQuery.trim(cookies[i]);
			if (cookie.substring(0, 10) == ('csrftoken' + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(10));
				break;
			}
		}
	}
	return cookieValue;
}

function success(title, message){
	$('#success-modal').modal('show')
    $('#title-success').text(title)
    $('#content-success').text(message)

}
