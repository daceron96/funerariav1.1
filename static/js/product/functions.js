$(document).ready(function(){
    $('#link-product').addClass('active');
})

const td_style_success = (value) =>{
    return `<td class='text-success fw-semibold'><i class='bi bi-patch-check-fill'></i> ${value} </td>`
}
const td_style_warning = (value) =>{
    return `<td class='text-warning fw-semibold'><i class='bi bi-patch-exclamation-fill'></i> 
    ${value} </td>`
}

const td_style_danger = (value) => {
    return `<td class='text-danger fw-semibold'><i class='bi bi-patch-exclamation-fill'></i>
        ${value} </td>`

}
const btn_state = (state,id) =>{
    return `<button type="button" class="btn ${state ? 'btn-danger' : 'btn-success'}" id="btn-state-suppllier" onClick='change_state_product(${id})'>
        <i class="bi ${state ? 'bi-x-circle' : 'bi-check-circle' }"></i> ${state ? "Dehabilitar" : "Habilitar"}
    </button>`

}