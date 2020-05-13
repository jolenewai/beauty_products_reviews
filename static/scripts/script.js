
// Example starter JavaScript for disabling form submissions if there are invalid fields
$(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    let forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    let validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);

  $(window).scroll(function(){
    $('#top-bar').toggleClass('scrolled', $(this).scrollTop() > 50);
    $('.navbar-toggler').toggleClass('shift-position', $(this).scrollTop() > 50)
    });

    AOS.init();

    feather.replace()
})();


