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

class Cliente extends Persona{
    static contadorClientes = 0;
    constructor(nombre,apellido,edad,fecharegistro){
        super(nombre,apellido,edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._fechaRegistro = fecharegistro;
    }
    get idCliente(){
        return this._idCliente;
    }
    get fecharegistro(){
        return this._fechaRegistro;
    }
    set fecharegistro(fecharegistro){
        this._fechaRegistro = fecharegistro;
    }
    toString(){
        return super.toString()+" "+this._idCliente+" "+this._fechaRegistro;
    }
}