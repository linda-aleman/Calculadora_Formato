function agregar(valor) {
    const pantalla = document.querySelector("input[name='pantalla']");
    pantalla.value += valor;
}

function limpiar() {
    const pantalla = document.querySelector("input[name='pantalla']");
    pantalla.value = ''; // Limpiar la pantalla completamente
}

function retroceder() {
    const pantalla = document.querySelector("input[name='pantalla']");
    pantalla.value = pantalla.value.slice(0, -1); // Eliminar el último carácter
}

function inicio(valor) {
    const pantalla = document.querySelector("input[name='pantalla']");
    if(pantalla == null || pantalla ==[]){
        pantalla.value = null;
    }
    if(pantalla != null || pantalla !=[]){
        pantalla.value += valor
    }

}