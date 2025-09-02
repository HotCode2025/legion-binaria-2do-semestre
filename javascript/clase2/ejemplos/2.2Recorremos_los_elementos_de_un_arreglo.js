//Recorremos los elementos de un arreglo
//Traemos de ejercicio anterior.
const autos = ['Ferrari', 'Renault', 'BMW']; // Esta es la sintaxis moderna

console.log(autos[0]);
console.log(autos[2]);

for(let i = 0; i < autos.length; i++) {
    console.log(i+' : '+autos[i]);
}
