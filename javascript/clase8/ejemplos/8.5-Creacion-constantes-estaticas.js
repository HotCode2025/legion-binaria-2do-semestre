class Persona{
    static contadorPersonas = 0;
    static get MAX_OBJ(){
        return 5; //simular constante
    }
    constructor(nombre,apellido){
        this._nombre=nombre;
        this._apellido=apellido;
        if(Persona.contadorPersonas < Persona.MAX_OBJ){
            this.idPersona=++Persona.contadorPersonas;
        }
        else{
            console.log("Se ha superado el maximo de objetos permitidos");
        }
    }
    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre=nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set apellido(nombre){
        this._apellido=apellido;
    }
    nombreCompleto(){
        return this.idPersona+" "+this._nombre+" "+this._apellido;
    }
    toString(){
        return this.nombreCompleto();
    }
    static saludar(){
        console.log("Saludos desde este metodo static");
    }
    static saludar2(persona){
        console.log(persona.nombre+" "+persona.apellido);
    }
}

// ---------------------------- //

class Empleado extends Persona{
    constructor(nombre,apellido,departamento){
        super(nombre,apellido);
        this._departamento=departamento;
    }
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento=this.departamento;
    }
    nombreCompleto(){
        return super.nombreCompleto()+", "+this._departamento;
    }
}

// ---------------------------- //

let persona1 = new Persona("Martin","Perez");
console.log(persona1.nombre);
let persona2 = (new Persona("Maria Laura", "Lara"))
console.log(persona2.nombre);
let empleado1 = new Empleado("Maria", "Gimenez", "Sistemas")
console.log(empleado1.nombre);

// ---------------------------- //

console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersonas);

// ---------------------------- //

let persona3 = new Persona("Carla", "Pertosi");
console.log(persona3.toString());
console.log(Persona.contadorPersonas);

// ---------------------------- //
// ---------------------------- //
// ---------------------------- //

console.log(Persona.MAX_OBJ);
//Persona.MAX_OBJ = 10; //no se modifica

let persona4 = new Persona("Franco", "Diaz");
console.log(persona4.toString())

let persona5 = new Persona("Liliana", "Paz");
console.log(persona5.toString())