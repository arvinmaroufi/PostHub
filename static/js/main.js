window.onload = function() {
    document.querySelector('.preloader-wrapper').style.display = 'none';
};

$(document).ready(function(){
    $('.feature-post-slider').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        autoplay: true,
        autoplayTimeout: 3000,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    });
});
