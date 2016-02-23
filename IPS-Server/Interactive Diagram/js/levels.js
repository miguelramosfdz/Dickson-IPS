
function endCb(elem) {
    if(elem[0].id=="container"){
        data("IPS");
        $('#car').fadeIn(400);
        $('.car-in').fadeOut(400);
        $(".level2").css('z-index', -1);
        $(".rpi-board").css('z-index', -1);
        $(".rpi-cam").css('z-index', -1);
        $(".cat45").css('z-index', -1);
    }
    else{
        $('#car').fadeOut(400);
        $('.car-in').fadeIn(400);
        $(".level2").css('z-index', 1);
        $(".rpi-board").css('z-index', 1);
        $(".rpi-cam").css('z-index', 1);
        $(".cat45").css('z-index', 1);
    }
}

function data(title){
    $('#title').text(title);
    $('#desc').text(as[title]);
    return 0;
}

