
package test;

import domain.Persona_Arreglos_parte_4_11_4;

public class TestArreglos_parte_5_y_6_Veamos_como_iterar_en_java_11_6 {
    public static void main(String[] args) {
        Persona_Arreglos_parte_4_11_4 personas[] = new Persona_Arreglos_parte_4_11_4[2];
        personas[0] = new Persona_Arreglos_parte_4_11_4("Ariel");
        personas[1] = new Persona_Arreglos_parte_4_11_4("Osvaldo");
        System.out.println("personas 0 = " + personas[0]);
        System.out.println("personas 1 = " + personas[1]);
        
        for(int i = 0; i < personas.length; i++){
            System.out.println("personas " + personas[i]);
        }
        //trabajamos con arreglos en la sintaxis resumida
        String frutas[] = {"Banana", "Pera", "Durazno"};
        for (int i = 0; i <frutas.length; i++){
            System.out.println("frutas = " +i+" = "+ frutas[i]);
        }
    }
}

