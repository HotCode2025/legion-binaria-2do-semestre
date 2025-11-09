class Persona{
    static contadorPersonas = 0;
    constructor(nombre,apellido,edad){
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }
    get _idPersona(){
        return this._idPersona;
    }
    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        return this._nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        return this._apellido;
    }
    get edad(){
        return this._edad;
    }
    set edad(edad){
        return this._edad;
    }
}

class Empleado extends Persona{
    static contadorEmpleados = 0;
    constructor(nombre,apellido,edad,sueldo){
        super(nombre,apellido,edad);
        this._idEmpleado = ++Empleado.contadorEmpleados;
        this._sueldo = sueldo;
    }
    get _idEmpleado(){
        return this._idEmpleado;
    }
    get sueldo(){
        this._sueldo;
    }
    set sueldo(sueldo){
        this._sueldo = sueldo;
    }
    toString(){
        return super.toString()+" "+this._idEmpleado+" "+this._sueldo;
    }
}