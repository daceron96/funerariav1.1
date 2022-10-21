var product_list = [];

function search_code() {
  let code = $("#code").val().trim();
  $(".is-invalid").removeClass("is-invalid");
  $(".is-valid").removeClass("is-valid");

  let exist = validate_code(code);

  if (!exist) {
    $.ajax({
      url: "/product/search/code",
      type: "GET",
      data: { code: code },

      success: (response) => {
        let exist_product = verify_product(response.code_list);
        if (!exist_product) {
          $(".is-invalid").removeClass("is-invalid");
          $("#code").addClass("is-valid").val("").focus();
          product_list.push(item(response));
          $("#loan_product_list").prepend(
            tr_table_add(...product_list.slice(-1))
          );
        }
      },
      error: (response) => {
        message_error(response.responseJSON);
      },
    });
  }
}


function create_loan() {
  form = $("#loan-form")
    .serializeArray()
    .reduce(function (a, z) {
      a[z.name] = z.value;
      return a;
    }, {});
  $.ajax({
    url: "/loan/create/",
    type: $("#loan-form").attr("method"),
    data: {
      csrfmiddlewaretoken: getCSRFToken(),
      form: JSON.stringify(form),
      list: JSON.stringify(product_list),
    },

    success: (response) => {
      reset_loan();
      $('.table-active').removeClass('table-active')
      $("#loan-table-list").prepend(tr_table_list(response));
			success("Registro de nuevo prestamo","El nuevo prestamo ha sido registrado exitosamente")

    },
    error: (response) => {
      $("#alert-list").addClass("visually-hidden");
      message_error(response.responseJSON.error);
      if (response.responseJSON.error["product"]) {
        $("#alert-list")
          .removeClass("visually-hidden")
          .text(response.responseJSON.error["product"]);
      }
    },
  });
}

function loan_detail(id) {
  $.ajax({
    url: `/loan/detail/${id}/`,
    type: "GET",
    success: (response) => {
      $('#reference-modal').empty().append(`<i class="bi bi-journal-minus fs-5"></i> Referencia: ${response.reference}`)
      $('#loan-type-modal').empty().append(`<i class="bi bi-box-seam fs-5 "></i> Tipo de salida: ${response.loan_type}`)
      $('#identifier-modal').empty().append(`<i class="bi bi-postcard fs-5 "></i> Número de documento: ${response.identifier}`)
      $('#name-client-modal').empty().append(`<i class="bi bi-person-badge fs-5 "></i> Nombre de cliente: ${response.name_client}`)
      $('#created-date-modal').empty().append(`<i class="bi bi-calendar-date fs-5 "></i> Fecha de registro: ${response.created_date}`)
      $('#quantity-modal').empty().append(`<i class="bi bi-boxes fs-5 "></i> Cantidad total: ${response.quantity}`)
      response.description.length  == 0 ?
			$('#description-modal').empty().append(`<i class="bi bi-chat-left-text fs-5 "></i> Descripcion: Sin descripcion`)
			:
			$('#description-modal').empty().append(`<i class="bi bi-chat-left-text fs-5 "></i> Descripcion: ${response.description}`)
      $('#loan-detail-list').empty()
      response.loan_list.map( detail => {
        $('#loan-detail-list').prepend(tr_table_detail(detail))
      })

      $("#loan-detail-modal").modal("show");
    },
  });
}

function filter_loan(){

	$.ajax({
		url : '/loan/filter/type/',
		method : 'GET',
		data : {pk : $('#select_category').val()},
		success : (response) =>{
			$('#loan-table-list').empty()
			response.data.forEach(data => {
				$('#loan-table-list').prepend(tr_table_list(data))
			})
      $('.table-active').removeClass('table-active')
		}
	})

}