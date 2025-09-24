// Uso de apply

let persona1 = {
  nombre: "Juan",
  apellido: "Perez",
  nombreCompleto: function (titulo, telefono) {
    return titulo + ": " + this.nombre + " " + this.apellido + " - " + telefono;
  },
};

let persona2 = {
  nombre: "Carlos",
  apellido: "Lara",
};

// A diferencia del metodo call, apply recibe un array con los argumentos
console.log(persona1.nombreCompleto("Licenciado", "123456789")); // uso normal del metodo del objeto persona1
console.log(
  persona1.nombreCompleto.apply(persona2, ["Ingeniero", "987654321"])
);
