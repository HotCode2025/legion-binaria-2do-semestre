// Ejercicio 1: Función que valide una contraseña 

function validatePassword(password) {

  if (password.length < 8) return false; // Debe tener mínimo 8 caracteres
  if (!/[A-Z]/.test(password)) return false; // debe tener al menos una mayúscula
  if (!/\d/.test(password)) return false; // debe tener al menos un número
  return true;

}



console.log(validatePassword("Abc12345")); // true

console.log(validatePassword("weak")); // false