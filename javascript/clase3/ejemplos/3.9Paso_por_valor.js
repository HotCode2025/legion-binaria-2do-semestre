//Tipos primitivos
let k = 10;
function cambiarValor(a){ //Paso por valor
    a = 20;
}
cambiarValor(k);
console.log(k);
//La variable no cambia en el paso por valor
