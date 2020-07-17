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


