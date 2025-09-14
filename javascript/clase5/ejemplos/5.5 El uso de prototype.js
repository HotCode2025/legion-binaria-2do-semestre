function Persona (nombre, apellido, email) {
        this.nombre = nombre
        this.apellido = apellido
        this.email = email
        this.nombreCompleto = () => { return this.nombre + ' ' + this.apellido} 
    }

let padre = new Persona('Leo', 'Lopez','lopez1@gmail.com')
let madre = new Persona('Laura','Contrera',"contrera1@gmail.com")
padre.nombre = 'Luis' // cambiamos el nombre de "Leo"
padre.telefono = 45616548789 // propiedad exclusiva del objeto "Leo Lopez"
console.log(padre)
console.log(padre.telefono) //usa la función de Leo Lopez
console.log(padre.nombreCompleto())
console.log(madre)
console.log(madre.telefono) // la propiedad no está definida 
console.log(madre.nombreCompleto())

//Uso de prototype
Persona.prototype.telefono = '11111111111'
console.log(padre)
console.log(madre.telefono)
madre.telefono = '5555555'
console.log(madre.telefono)