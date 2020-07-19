var counter=-1;

async function scroll(){
    // while(phrase != "richard"){
    //     $("#change").val(phrase);
    //     console.log("test");
    // }
    let words = [" scary "," diverse "," huge ", " salty ", " chilly ", " wet "," blue "," bright "," dark "," deep ", " unknown "]
    counter++;
    if(words[counter] != undefined){
    document.getElementById("change").innerHTML = words[counter];}
    else{
        counter=-1;
    }
    // $("#change").slideUp("slow");
}

let inty = setInterval(scroll,1500);
// setTimeout(() => { clearInterval(inty);}, 16500);


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
            // $(".navbar-toggler").css("display","inline!important");
            // $(".navbar-toggler").show();
            // $(".navbar-toggler").click(function(){
            //     $(".navbar-nav").show();
            //     $(".navbar-nav").css("color","black!important");
            //     $(".navbar-nav").css("font-size","2rem");
            // })
        }
        else{
            $(".navbar-fixed-top").removeClass("sticky-top");
            $("#navbarNav").show();
            $("#brandgone").show();
            $(".navbar-nav").show();
            // $(".navbar-nav").css("font-size","16px");
            // $(".navbar-toggler").hide();
        }
    });
});
function reDirect(){
    var url = "https://discord.com/api/oauth2/authorize?client_id=733765721934266469&permissions=8&scope=bot"
    window.location.href = url;
}
function linkedIn(clickedID){
    if(clickedID == "spLinked"){
        window.location.href = "https://www.linkedin.com/in/sachet-patil/"
    }
    else if(clickedID == "mcLinked"){
        window.location.href = "https://www.linkedin.com/in/mohit-chhaya-54582219b//"
    }
    else if(clickedID == "ppLinked"){
        window.location.href = "https://www.linkedin.com/in/pranish-pantha/"
    }
    else if(clickedID == "msLinked"){
        window.location.href = "https://www.linkedin.com/in/maanav-singh-60a407129/"
    }
}
function gitHub(clickedID){
    if(clickedID == "spGithub"){
        window.location.href = "https://github.com/SkPatil22"
    }
    else if(clickedID == "mcGithub"){
        window.location.href = "https://github.com/mrchhaya"
    }
    else if(clickedID == "ppGithub"){
        window.location.href = "https://github.com/Pranish-Pantha"
    }
    else if(clickedID == "msGithub"){
        window.location.href = "https://github.com/MaanavS16"
    }
}
// var divWidth = $("changediv").width();
// var fSize = $(".h1").css("fontsize")
// console.log(fSize);
// while($(".h1").width() > divWidth){
//     console.log(fSize);
//     $(".h1").css("font-size", fSize-=2);
//     $("#change").css("font-size",fSize-=2);
// }
// $(this).scrollTop() > $nav.height()