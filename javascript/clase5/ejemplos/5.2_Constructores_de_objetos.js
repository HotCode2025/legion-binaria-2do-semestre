
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 28,
    idioma: 'es',
     get lang(){
        return this.idioma.toUpperCase();//Convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){//metodo o funcion en JavaScript
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){ //Este es el metodo get
        return 'El nombre es: '+this.nombre+', Edad: '+this.edad;
    }
}

console.log('Comenzamos a utilizar el metodo get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email){//Constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
}
let padre = new Persona3('leo', 'Lopez','lopez@gmail.com');
padre.nombre = 'Luis';
console.log(padre);

let madre = new Persona3('Laura', 'Contreras', 'contrerasl@gmail.com');
console.log(madre);