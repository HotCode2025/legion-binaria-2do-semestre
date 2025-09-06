// Ejemplo 4: Como acceder a las propiedades de los objetos.

let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad:30,
    nombreCompleto: function(){
        return this.nombre+' '+this.apellido;
    }
}

//Accedemos como si fuera un arreglo

console.log(persona['apellido']); 

//for in 
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}