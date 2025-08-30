// Etiquetas Labels
inicio: for (let contador = 0; contador < 10; contador++) {
  if (contador % 2 != 0) {
    break inicio; // Salta los impares
  }
  console.log(contador); // Muestra todos los pares
}
console.log("Termina el ciclo al encontrar los pares");
