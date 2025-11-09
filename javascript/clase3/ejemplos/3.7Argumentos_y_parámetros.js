//Funcion típo expresión
let sumar = function(a = 4, b = 8) {
    console.log(arguments[0]); //muestra el parametro de: a
    console.log(arguments[1]); //muestra el parametro de: b
    return a + b + arguments[2];
}
let resultado = sumar(3, 2, 9);
console.log(resultado);

