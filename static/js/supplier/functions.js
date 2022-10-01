$(document).ready(function(){
    $('#link-supplier').addClass('active');
})




const btn_state = (state,id) =>{
    return `<button type="button" class="btn ${state ? 'btn-danger' : 'btn-success'}" id="btn-state-suppllier" onClick='change_state_supplier(${id})'>
        <i class="bi ${state ? 'bi-x-circle' : 'bi-check-circle' }"></i> ${state ? "Dehabilitar" : "Habilitar"}
    </button>`

}