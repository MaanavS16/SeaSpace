var counter=-1;

async function scroll(){
    // while(phrase != "richard"){
    //     $("#change").val(phrase);
    //     console.log("test");
    // }
    counter++;
    let words = [" Scary "," Diverse "," HUGE "]
    document.getElementById("change").innerHTML = words[counter];
    // $("#change").slideUp("slow");
}

let inty = setInterval(scroll,2000);
setTimeout(() => { clearInterval(inty);}, 6000);


