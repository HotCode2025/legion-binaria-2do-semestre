//Ejercicio 1: Diseñe un programa que permita ingresar una cadena de caracteres, y detecte cuántas vocales tiene.

let cadena1 = "Buenas tardes";

let contador = 0;

let texto = cadena1.toLowerCase();

for (let i = 0; i < texto.length; i++) {
  if (
    texto[i] === "a" ||
    texto[i] === "e" ||
    texto[i] === "i" ||
    texto[i] === "o" ||
    texto[i] === "u"
  ) {
    contador++;
  }
}

console.log("Ejercicio 1");

console.log("Total de vocales: " + contador);

// Ejercicio 2: Calcular la longitud de 2 cadenas de caracteres, y mostrar la cadena con la mayor longitud.

let cadena2 = "Buenas tardes";

let cadena21 = "Buen dia";

let longitud1 = cadena1.length;

let longitud2 = cadena21.length;

console.log("Ejercicio 2");

if (longitud1 > longitud2) {
  console.log("La cadena: " + cadena2 + ", es la cadena con mayor longitud");
} else if (longitud1 < longitud2) {
  console.log("La cadena: " + cadena21 + ", es la cadena con mayor longitud");
} else {
  console.log("Ambas cadenas tienen la misma longitud");
}

//Ejercicio 3: Diseñe un algoritmo cuya entrada sea una Cadena, y un número entero N, cuya función sea generar la cadena dada N veces.

let cadena3 = "Hola";

let entero = 4;

console.log("Ejercicio 3");

for (let numero = 0; entero > 0; entero--) {
  console.log(cadena3);
}

//Ejercicio 4: Diseñe un algoritmo que elimine los espacios en blanco de un texto.

let cadena4 = "Que tal tu dia";

let textoSinEspacio = cadena4.replace(/\s+/g, "");

console.log("Ejercicio 4");
console.log("Texto sin espacios: " + textoSinEspacio);

//Ejercicio 5: Cambiar una cadena de caracteres, al revés

let cadena5 = "Programacion";

let cadenaInvertida5 = "";

for (let i = cadena5.length - 1; i >= 0; i--) {
  cadenaInvertida5 += cadena5[i];
}

console.log("Ejercicio 5");
console.log("La cadena invertida es: " + cadenaInvertida5);

//Ejercicio 6: Diseñar un algoritmo que tomando como entrada una cadena de texto nos devuelva si es o no un palíndromo.
//Se conoce que se denomina palíndromo a una palabra o frase que, ignorando los blancos,
//se lee igual de izquierda a derecha que de derecha a izquierda.

let cadena6 = "Reconocer";

let cadenaMinusculas6 = cadena6.toLowerCase();

let cadenaInvertida6 = "";

for (let i = cadenaMinusculas6.length - 1; i >= 0; i--) {
  cadenaInvertida6 += cadenaMinusculas6[i];
}

console.log("Ejercicio 6");

if (cadenaMinusculas6 == cadenaInvertida6) {
  console.log("La palabra es palindroma");
} else {
  console.log("La palabra no es palindroma");
}

//Ejercicio 7: Ingresar una frase y modificarla convirtiendo el primer carácter de cada palabra si esta fuera una letra,
// de minúsculas a mayúsculas.

let frase7 = "hola mundo! 123abc xyz";
let resultado7 = "";
let inicioDePalabra7 = true;

for (let i = 0; i < frase7.length; i++) {
  let ch = frase7[i];

  let esLetraMinus = ch >= "a" && ch <= "z";
  let esLetraMayus = ch >= "A" && ch <= "Z";
  let esLetra = esLetraMinus || esLetraMayus;

  if (inicioDePalabra7 && esLetraMinus) {
    resultado7 += ch.toUpperCase();
    inicioDePalabra7 = false;
  } else {
    resultado7 += ch;
    inicioDePalabra7 = !esLetra;
  }
}

console.log("Ejercicio 7");
console.log(resultado7);

//Ejercicio 8: Sustituir todos los espacios en blanco de una frase por un asterisco (*).

let frase8 = "Hola como estas";

let fraseModificada8 = "";

for (let i = 0; i < frase8.length; i++) {
  if (frase8[i] === " ") {
    fraseModificada8 += "*";
  } else {
    fraseModificada8 += frase8[i];
  }
}
console.log("Ejercicio 8");
console.log("Frase con asteriscos: " + fraseModificada8);

//Ejercicio 9: Leer una frase y contar el número de vocales (de cada una) que aparecen.

let frase9 = "Frase con muchas vocales";

let fraseMinuscula9 = frase9.toLowerCase();

let contadorA = 0,
  contadorE = 0,
  contadorI = 0,
  contadorO = 0,
  contadorU = 0;

for (let i = 0; i < fraseMinuscula9.length; i++) {
  if (fraseMinuscula9[i] === "a") {
    contadorA++;
  } else if (fraseMinuscula9[i] === "e") {
    contadorE++;
  } else if (fraseMinuscula9[i] === "i") {
    contadorI++;
  } else if (fraseMinuscula9[i] === "o") {
    contadorO++;
  } else if (fraseMinuscula9[i] === "u") {
    contadorU++;
  }
}
console.log("Ejercicio 9");
console.log("Cantidad de A: " + contadorA);
console.log("Cantidad de E: " + contadorE);
console.log("Cantidad de I: " + contadorI);
console.log("Cantidad de O: " + contadorO);
console.log("Cantidad de U: " + contadorU);

//Ejercicio 10: Realizar un programa que permita contabilizar cuantas veces una subcadena se repite dentro de una frase.
let frase10 = "anana ana ana banana";
let sub10 = "ana";
let conteo10 = 0;

if (sub10.length > 0) {
  for (let i = 0; i <= frase10.length - sub10.length; i++) {
    let coincide = true;

    for (let j = 0; j < sub10.length; j++) {
      if (frase10[i + j] !== sub10[j]) {
        coincide = false;
        break;
      }
    }

    if (coincide) {
      conteo10++;
    }
  }
}
console.log("Ejercicio 10");
console.log("La subcadena aparece: " + conteo10 + " veces");
