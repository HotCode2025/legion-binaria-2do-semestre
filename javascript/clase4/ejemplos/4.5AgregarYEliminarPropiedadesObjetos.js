console.log("creando un objeto");
const persona = {
  nombre: "Luis",
  apellido: "Perez",
  edad: 23,
  direccion: "Calle 123",
  telefono: "123456789",
};

// cambiamos dinamicamente el valor de una propiedad del objeto
console.log("cambiando el valor de la propiedad 'nombre'");
persona.nombre = "Pedro";

// nota: Si al asignarle un nuevo valor a una propiedad que no existe, se creara una nueva propiedad con el nuevo valor
console.log("cambiamos y eliminamos un error");
persona.nombres = "Luis";
console.log(persona);
// {
//   nombre: "Pedro",
//   apellido: "Perez",
//   edad: 23,
//   direccion: "Calle 123",
//   telefono: "123456789",
//   nombres: "Luis" <------- Nueva propiedad
// };

// eliminar una propiedad
delete persona.nombres; // Se elimina la propiedad 'nombres'
console.log(persona);
// {
//   nombre: "Pedro",
//   apellido: "Perez",
//   edad: 23,
//   direccion: "Calle 123",
//   telefono: "123456789"
// };