jQuery(document).ready(function () {
    "use strict";
    $('#slider-carouesel').caroufredsel({
        responsive: true,
        width: '100%',
        circular: true,
        scroll: {
            items: 1,
            duration: 600,
            pauseOnHover: true
        },
        auto: true,
        items: {
            visible: {
                min: 1,
                max: 1
            },
            height: "variable"
        },
        pagination: {
            container: ".sliderpager",
            pageAchorBuilder: false
        }
    })
});

// var prevScrollpos = window.pageYOffset;
// window.onscroll = function() {
//     var currentScrollPos = window.pageYOffset;
//     if (prevScrollpos > currentScrollPos) {
//         document.getElementById("navbar").style.top = "0";
//     } else {
//         document.getElementById("navbar").style.top = "-100px";
//     }
//     prevScrollpos = currentScrollPos;
// }

// For single Product
var MainImg = document.getElementById('MainImg')
var smallImg = document.getElementsByClassName('small-img');

smallImg[0].onclick = function () {
    MainImg.src = smallImg[0].src;
}
smallImg[1].onclick = function () {
    MainImg.src = smallImg[1].src;
}
smallImg[2].onclick = function () {
    MainImg.src = smallImg[2].src;
}
smallImg[3].onclick = function () {
    MainImg.src = smallImg[3].src;
}

// gallery part
baguetteBox.run(".tz-gallery");
