
let product_list = []


function get_product(){
    let code = $('#code').val().trim()
    let quantity = $('#quantity').val().trim()
    
    var bandera = validate_code(code,quantity)
    if(bandera){
        bandera = search_product(code,quantity)
    }
    if(bandera){
        $.ajax({
            url : `/product/get/${code}/`,
            type : 'GET',
            success : (response) => {
                $('#code').removeClass('is-invalid').val('').focus()
                $('#quantity').removeClass('is-invalid').val('')
                $('#alert-list').addClass('visually-hidden')
                product_list.push(item(response,quantity))
                $('#input_product_list').prepend(tr_table_add(...product_list.slice(-1)))
            },
            error : (response) => {
                message_error(response.responseJSON.error)

            }
        })
    }
    
}

function input_detail(input_id){

    $.ajax({
        url : `/input/detail/${input_id}/`,
        method : "GET",
        success : (response) => {
            $('#input-detail-list').empty()
			$('#reference-modal').empty().append(`<p><i class="bi bi-clipboard-minus-fill fs-5"></i> ${response.reference}</p>`)
			$('#supplier-modal').empty().append(`<p><i class="bi bi-person-circle fs-5 "></i>  ${response.supplier}</p>`)
			$('#quantity-modal').empty().append(`<p><i class="bi bi-boxes fs-5"></i> ${response.quantity}</p>`)
			$('#created-modal').empty().append(`<p><i class="bi bi-calendar-date-fill fs-5"></i> ${response.created_date}</p>`)
            $('#btn-deposit').remove()
            $('#btn-update-input').remove()
            response.description === '' ? 
			$('#description-modal').empty().append(`<p><i class="bi bi-body-text"></i> Sin descripcion</p>`)
            :
			$('#description-modal').empty().append(`<p><i class="bi bi-body-text"></i> ${response.description}</p>`)
            
            if(response.in_wait){
                if(!response.created_qr){
                    $('#btn-detail-modal').append(btn_update_deposit(response.id)) 
                }
                $('#btn-detail-modal').append(btn_deposit(response.id)) 
            }
            response.product_list.forEach(element => {
                $('#input-detail-list').prepend(tr_detail_list(element))
            });
            $('#input-detail-modal').modal('show')
            // $('#btn-update-input').attr("onClick", `input_get_detail(${response.id})`)
            $('#btn-save').attr("onClick", `update_input(${response.id})`)


        }
    })
    
}

function input_get_detail(input_id){

    $.ajax({
        url : `/input/detail/${input_id}/`,
        method : "GET",

        success: (response) => {
            $('#input-detail-modal').modal('hide')
            //lanza modal de formulario con los datos correspondientes
            $('#input-form-modal').modal('show')
            $('#reference').val(response.reference)
            $('#supplier').val(response.supplier)

            //llena el array con objetos de tipo producto
            response.product_list.forEach(element => {
                product_list.push(item(element,element.quantity))
                $('#input_product_list').prepend(tr_table_add(...product_list.slice(-1)))
            })
            
        }
    })
}

function input_get_detail_deposit(input_id){

    $.ajax({
        url : `/input/deposit/${input_id}/`,
        method : "GET",
        
        success : (response) =>{
            $('#input-detail-modal').modal('hide')
            $('#deposit-form-modal').modal('show')
            $('#btn-save-deposit').attr('onClick', `send_deposit(${input_id})`)
            $('#reference-deposit-modal').empty().append(`<p><i class="bi bi-clipboard-minus-fill fs-5"></i> ${response.reference}</p>`)
			$('#supplier-deposit-modal').empty().append(`<p><i class="bi bi-person-circle fs-5 "></i>  ${response.supplier}</p>`)
			console.log(response)
            $('#btn-download').attr('href',`/${response.url}`)
            product_list = response.data
            product_list.forEach((element) => {
                $('#input_deposit_list').prepend(tr_table_deposit(element))
                element.deposit = 0
            })
        }
    })


}


function create_input(){
    
    form = {
        reference : $('#reference').val(),
        supplier : $('#supplier').val()
    }
    $.ajax({
        url : '/input/create/',
        type : 'POST',
        data : {
                csrfmiddlewaretoken : getCSRFToken() ,
                form : JSON.stringify(form),
                list : JSON.stringify(product_list)
            },
    
        success : (response) => {
            reset_input()
			$('.table-active').removeClass('table-active');
            $('#input-table-list').prepend(tr_list(response))
            success('Registro de nueva entrada', 'La nueva entrada ha sido registrada exitosamente')
        },
        error : (response) => {
            message_error(response.responseJSON.error)
            if(response.responseJSON.error['product']){
                $('#alert-list').removeClass('visually-hidden').text(response.responseJSON.error['product'])

            }
        }
    })

}


function update_input(input_id){

    $.ajax({
        url : `/input/update/${input_id}/`,
        type : 'POST',
        data : {
                csrfmiddlewaretoken : getCSRFToken() ,
                list : JSON.stringify(product_list)
            },
        success : (response) => {
            reset_input()
			$('.table-active').removeClass('table-active');
            $(`#tr-list-${response.id}`).addClass('table-active')
            $(`#quantity-${response.id}`).text(response.quantity)
            
            success('Actualización de entrada', 'La entrada ha sido modificada exitosamente')
        },
        error : (response) => {
            message_error(response.responseJSON.error)
            if(response.responseJSON.error['product']){
                $('#alert-list').removeClass('visually-hidden').text(response.responseJSON.error['product'])

            }
        }
    })
}

// TODO falta validar y enviar una lista con los codigos a ingresar al back
function send_deposit(input_id){
    
    $.ajax({
        url : `/input/deposit/${input_id}/`,
        method : "POST",
        data : {
            csrfmiddlewaretoken : getCSRFToken() ,
        },
        success : (response) =>{
            $('.table-active').removeClass('table-active')
            $(`#tr-list-${response.id}`).addClass('table-active')
            $(`#td-state-${response.id}`).empty().append(
                `<i class="bi bi-patch-check-fill text-success"></i>`
            )
            reset_input('deposit')
            success("Ingreso de productos","El ingreso de los productos ha sido exitoso")
        }
    })

}


