// let persona3 = new Persona('Carla', 'Ponce'); Esto no se debe hacer, Persona is not defined
class Persona {
  constructor(nombre, apellido) {
    this._nombre = nombre;
    this._apellido = apellido;
  }

  get nombre() {
    return this._nombre;
  }

  set nombre(nombre) {
    this._nombre = nombre;
  }

  get apellido() {
    return this._apellido;
  }

  set apellido(apellido) {
    this._apellido = apellido;
  }
}

class Empleado extends Persona {
  //clase hija
  constructor(nombre,apellido,departamento) {
    super(nombre,apellido)
    this._departamento = departamento;
  }

  get departamento() {
    return this._departamento;
  }

  set departamento(departamento) {
    this._departamento = departamento;
  }
}

let persona1 = new Persona("Martín", "Perez");
console.log(persona1.nombre);
console.log(persona1.apellido);

persona1.nombre = "Juan Carlos";
persona1.apellido = "Gómez";
console.log(persona1.nombre);
console.log(persona1.apellido);

// Persona 2
let persona2 = new Persona("Carlos", "Lara");
console.log(persona2.nombre);
console.log(persona2.apellido);

persona2.nombre = "María Laura";
persona2.apellido = "Fernández";
console.log(persona2.nombre);
console.log(persona2.apellido);

let empleado1 = new Empleado('María','Gimenez','Sistemas')
console.log(empleado1)
console.log(empleado1._nombre)
