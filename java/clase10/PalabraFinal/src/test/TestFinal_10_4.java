/*
Uso de la palabra Final
Esta palabra tiene diferentes significados dependiendo donde
se aplique:
    variables: Evita cambiar el valor que almacena la variable
    métodos: Evita que se modifique la definición o el comportamineto
            de un método desde una subclase (hija)
    clases: Evita que se creen las clases hijas
Otra caracteristica es que normalmente, caundo trabajamos con variables
se combina con el modificador de acceso estático para convertir una
variable en una constaante, es decir que no se puede modificar su valor,
el ejemplo de esto es la clase Math en la cúal todos sus atributos
son de tipo static y final, es por esto que la variable pi* se conoce
como una constante.
*/
package test;

import domain.Persona_10_4;

public class TestFinal_10_4 {
    public static void main(String[] args) {
        final int miDni = 38596854;
        System.out.println("miDni = " + miDni);
        //MIdNI = 20312321; No se puede modificar
        //Persona.CONSTANTE_AQUI = 9; //No se modifica
        System.out.println("Mi atributo constatne es: " +Persona_10_4.CONSTANTE_AQUI);
        
        final Persona_10_4 persona1 = new Persona_10_4();
        //persona1 = new Persona(); No se puede asignar una nueva referencia
        persona1.setNombre("Ariel Betancud");
        System.out.println("persona1 nombre: " +persona1.getNombre());
        persona1.setNombre("Liliana");
        System.out.println("persona1 nombre: " +persona1.getNombre());
    }
}
