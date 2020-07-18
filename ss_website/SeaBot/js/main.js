var counter=-1;

async function scroll(){
    // while(phrase != "richard"){
    //     $("#change").val(phrase);
    //     console.log("test");
    // }
    counter++;
    let words = [" Scary "," Diverse "," HUGE ", " Salty ", " Chilly ", " Wet ", " Tranquil "," Blue "," Bright "," Dark "," Deep "]
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
            $("#navbar-nav").hide();
        }
        else{
            $(".navbar-fixed-top").removeClass("sticky-top");
            $("#navbarNav").show();
            $("#brandgone").show();
            $("#navbar-nav").show();
        }
    });
});
// $(this).scrollTop() > $nav.height()