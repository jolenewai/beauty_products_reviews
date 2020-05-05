$(window).scroll(function(){
    $('#top-bar').toggleClass('scrolled', $(this).scrollTop() > 50);
    $('.navbar-toggler').toggleClass('shift-position', $(this).scrollTop() > 50)
});