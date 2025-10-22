// Ejercicio 1
//Imprimir numeros del 0 al 5 con el ciclo While

let i1 = 0;
console.log("Ejercicio 1");

while (i1 <= 5) {
  console.log(i1);
  i1++;
}

// Ejercicio 2
//Imprimir numeros del 5 al 0 con el ciclo While

let numero2 = 5;

console.log("Ejercicio 2");
while (numero2 >= 0) {
  console.log(numero2);
  numero2--;
}

// Ejercicio 3
//Diseñar un programa que al ingresar el año, nos devuelva
//por consola si es un año bisiesto o no, repetir la accion
//hasta que el usuario lo decida.

usuario3 = 1;

año3 = 1948;

console.log("Ejercicio 3");

while (usuario3 == 1) {
  if (año3 % 4 == 0) {
    console.log("El año " + año3 + " es bisiesto.");
  } else {
    console.log("El año " + año3 + " no es bisiesto.");
  }

  usuario3++;
}

// Ejercicio 4
//Calcular la suma de los "N" primeros numeros

let num4 = 10;
let i4 = 1;
let suma4 = 0;

while (i4 <= num4) {
  suma4 = suma4 + i4;
  i4++;
}
console.log("Ejercicio 4");
console.log("La suma de los primeros " + num4 + " numeros es: " + suma4);

// Ejercicio 5
//Leer el numeros e imprimir si es positivo, neutros o negativos
let i5 = 0;
let num5 = 0;

console.log("Ejercicio 5");
for (let i5 = 0; i5 < 1; i5++) {
  if (num5 > 0) {
    console.log("El numero es positivo");
  } else if (num5 < 0) {
    console.log("El numero es negativo");
  } else {
    console.log("El numero es neutro");
  }
}

// Ejercicio 6
//Supongamos que se tiene un conjunto de calificaciones de un grupo de 10 alumnos.
//Realizar un algoritmo para calcular la calificacion promedio
//y la calificación mas baja y la mas alta

let notas6 = [99, 85, 65, 73, 65, 94, 95, 78, 86, 87];

let suma6 = 0;
let notaBaja6 = notas6[0];
let notaAlta6 = notas6[0];

for (let i = 0; i <= 9; i++) {
  suma6 += notas6[i];

  if (notas6[i] < notaBaja6) {
    notaBaja6 = notas6[i];
  } else if (notas6[i] > notaAlta6) {
    notaAlta6 = notas6[i];
  }
}

console.log("La calificación promedio es: " + suma6 / 10);
console.log("La calificación más baja es: " + notaBaja6);
console.log("La calificación más alta es: " + notaAlta6);
