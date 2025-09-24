//Agregamos metodos al constructor del objeto

function Persona3(nombre, apellido, email){//Constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('leo', 'Lopez','lopez@gmail.com');
padre.nombre = 'Luis';
console.log(padre);
console.log(padre.nombreCompleto());//Utilizamos la funcion

let madre = new Persona3('Laura', 'Contreras', 'contrerasl@gmail.com');
console.log(madre);
console.log(madre.nombreCompleto());