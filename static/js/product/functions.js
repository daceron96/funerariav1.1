$(document).ready(function () {
  $("#link-product").addClass("active");
});

function auto_complete() {
  var availableTags = [
    "ActionScript",
    "AppleScript",
    "Asp",
    "BASIC",
    "C",
    "C++",
    "Clojure",
    "COBOL",
    "ColdFusion",
    "Erlang",
    "Fortran",
    "Groovy",
    "Haskell",
    "Java",
    "JavaScript",
    "Lisp",
    "Perl",
    "PHP",
    "Python",
    "Ruby",
    "Scala",
    "Scheme",
  ];
  $( "#input_search" ).autocomplete({
    source: availableTags
  });
}


function validate_style(data){
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
    stock_wait = td_style_warning(data.stock_wait);
  }

  return {stock_cellar : stock_cellar, stock_loan: stock_loan, stock_wait: stock_wait}

}