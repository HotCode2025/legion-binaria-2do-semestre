let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30,
    nombreCompleto: function() {
        return this.nombre+' '+this.apellido;
    }
}

console.log(persona.nombreCompleto());
