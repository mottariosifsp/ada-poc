
var disponilibity_done = document.currentScript.getAttribute("disponilibity_done");
var lang = document.currentScript.getAttribute("data-lang");

if(disponilibity_done == 'False') {
    $(document).ready(function() {
        $('.overlay').css('display', '');
        $('#container div.card').prop('disabled', true);
        $('#container div.card').css('opacity', '0.4');
    });
}



function fpa_blockk_animation() {
    window.scrollTo({
        top: $("#fpa-blockk").offset().top - $(".navbar").outerHeight() - 30,
        behavior: "smooth",
    });
}

