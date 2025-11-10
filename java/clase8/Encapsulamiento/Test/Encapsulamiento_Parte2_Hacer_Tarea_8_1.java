
package Test;

import dominio.Encapsulamiento_Parte_1_7_6;

public class Encapsulamiento_Parte2_Hacer_Tarea_8_1 {
    public static void main(String[] args) {
        Encapsulamiento_Parte_1_7_6 persona1 = new Encapsulamiento_Parte_1_7_6("Osvaldo", 57.000, false);
        
        //Modificar a través de los métodos
        persona1.setNombre("Juan Ignacio");
        // persona1.nombre = "Juan Ignacio"; //Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre); //Error
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial
        //e imprimir, luego modificar sus valores y volver a imprimir
        
        Encapsulamiento_Parte_1_7_6 persona2 = new Encapsulamiento_Parte_1_7_6("Osvaldo", 57.000, false);
        persona2.setNombre("Cristian Jesus");
        System.out.println("persona2 su nombre es: "+persona2.getNombre());
        System.out.println("persona2 el sueldo es de: "+persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: "+persona2.isEliminado());
        
        
    }
}
