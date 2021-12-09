let menu = document.getElementById("menu")
let header = document.getElementById("header")
let nav = document.getElementById("nav")

function ajustarTamañoHeader(){
    header.style.height = "60px"
}

menu.addEventListener("click", function(){
    if(header.style.height == "60px" || header.offsetHeight == 60) {
        header.style.height = "100%";
    } else {
        ajustarTamañoHeader();
    }
    
})

window.addEventListener("resize", function(){
    let ancho = document.documentElement.clientWidth

    if(ancho > 480) {
        header.style = ""
    }
})