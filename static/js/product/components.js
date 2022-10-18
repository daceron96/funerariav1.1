const td_style_success = (value) => {
  return `<td class='text-success fw-semibold'><i class='bi bi-patch-check-fill'></i> ${value} </td>`;
};
const td_style_warning = (value) => {
  return `<td class='text-warning fw-semibold'><i class='bi bi-patch-exclamation-fill'></i> 
  ${value} </td>`;
};

const td_style_danger = (value) => {
  return `<td class='text-danger fw-semibold'><i class='bi bi-patch-exclamation-fill'></i>
      ${value} </td>`;
};
const btn_state = (state, id) => {
  return `<button type="button" class="btn ${
    state ? "btn-danger" : "btn-success"
  }" id="btn-state-suppllier" onClick='change_state_product(${id})'>
      <i class="bi ${state ? "bi-x-circle" : "bi-check-circle"}"></i> ${
    state ? "Dehabilitar" : "Habilitar"
  }
  </button>`;
};

const state_style = (state, id) => {
  let item = "";
  if (state) {
    item = `<td id='td-state-${id}'><i class='bi bi-check-circle-fill text-success'></i></td>`;
  } else {
    item = `<td id='td-state-${id}'><i class='bi bi-x-circle-fill text-danger'></i></td>`;
  }
  return item;
};

const tr_table_list = (data) => {
  let state = state_style(data.state, data.id);
  let stock_cellar = "";
  let stock_loan = "";
  let stock_wait = "";
  
  //style stock cellar according to your quantity
  if (data.stock_cellar > 10) {
    stock_cellar = td_style_success(data.stock_cellar);
  } else if (data.stock_cellar == 0) {
    stock_cellar = td_style_danger(data.stock_cellar);
  } else {
    stock_cellar = td_style_warning(data.stock_cellar);
  }

  //style stock loan according to your quantity
  if (data.stock_loan == 0) {
    stock_loan = td_style_success(data.stock_loan);
  } else {
    stock_loan = td_style_warning(data.stock_loan);
  }

  //style stock wait according to your quantity
  if (data.stock_wait == 0) {
    stock_wait = td_style_success(data.stock_wait);
  } else {
    stock_wait = td_style_warning(data.stock_loan);
  }

  return `
    <tr class=' text-muted' id='tr-${data.id}' onClick=product_detail(${data.id})>
    ${state}
    <th> ${data.code} </th>
    <td id='td-name-${data.id}'> ${data.name} </td>
    <td id='td-category-${data.id}'> ${data.category} </td>
    ${stock_cellar}
    ${stock_wait}
    ${stock_loan}
    </tr> 
  `

};
