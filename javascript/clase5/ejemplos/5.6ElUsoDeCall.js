// Use de call

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

console.log(persona1.nombreCompleto("Licenciado", "123456789")); // uso normal del metodo del objeto persona1
console.log(persona1.nombreCompleto.call(persona2, "Ingeniero", "987654321")); // uso del metodo del objeto persona1 con el objeto persona2. Es decir, dentro del metodo se rreplaza this por persona2.
// Ej: Dentro del metodo "persona1.nombreCompleto" la variable "this.nombre" pasara a "persona2.nombre". Se debe asegurar que el objeto que se usa como reemplazo de "this" tenga las propiedades que se usan en el metodo
