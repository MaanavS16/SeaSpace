var counter=-1;

async function scroll(){
    // while(phrase != "richard"){
    //     $("#change").val(phrase);
    //     console.log("test");
    // }
    counter++;
    let words = [" scary "," diverse "," HUGE ", " salty ", " chilly ", " wet ", " tranquil "," blue "," bright "," dark "," deep "]
    document.getElementById("change").innerHTML = words[counter];
    // $("#change").slideUp("slow");
}

let inty = setInterval(scroll,1500);
setTimeout(() => { clearInterval(inty);}, 16500);


const navbar = $("#1nav");
const txt = $("#brandgone");


$(function () {
    $(document).scroll(function () {
        var $nav = $(".navbar-fixed-top");
        var bln = $(this).scrollTop() >= $nav.height();
        console.log(bln);
        if(bln){
            $(".navbar-fixed-top").addClass("sticky-top");
            $("#navbarNav").hide();
            $("#brandgone").hide();
            $(".navbar-nav").hide();
            $(".navbar-toggler").show();
            $(".navbar-toggler").click(function(){
                $(".navbar-nav").show();
                $(".navbar-nav").css("color","black!important");
                $(".navbar-nav").css("font-size","2rem");
            })
        }
        else{
            $(".navbar-fixed-top").removeClass("sticky-top");
            $("#navbarNav").show();
            $("#brandgone").show();
            $(".navbar-nav").show();
            $(".navbar-nav").css("font-size","16px");
            $(".navbar-toggler").hide();
        }
    });
});


// var divWidth = $("changediv").width();
// var fSize = $(".h1").css("fontsize")
// console.log(fSize);
// while($(".h1").width() > divWidth){
//     console.log(fSize);
//     $(".h1").css("font-size", fSize-=2);
//     $("#change").css("font-size",fSize-=2);
// }
// $(this).scrollTop() > $nav.height()