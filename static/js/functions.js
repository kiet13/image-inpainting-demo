$('li > a').click(function() {
    $('a').removeClass();
    $(this).addClass('active');
});