class Persona{
    static contadorPersonas = 0;
    constructor(nombre,apellido){
        this._nombre=nombre;
        this._apellido=apellido;
        this.idPersona=++Persona.contadorPersonas;
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

