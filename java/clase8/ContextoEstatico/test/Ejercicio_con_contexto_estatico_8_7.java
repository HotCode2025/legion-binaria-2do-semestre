
package test;

import domain.Contexto_estatico_práctica_Parte_1_8_5;

public class Ejercicio_con_contexto_estatico_8_7 {
    private int contador;

    public static void main(String[] args) {
        Contexto_estatico_práctica_Parte_1_8_5 persona1 = new Contexto_estatico_práctica_Parte_1_8_5("Ariel");
        System.out.println("persona1 = " + persona1);
        Contexto_estatico_práctica_Parte_1_8_5 persona2 = new Contexto_estatico_práctica_Parte_1_8_5("Naty");
        System.out.println("persona2 = " + persona2);
        imprimir(persona1);
        imprimir(persona2);
        // this.contador = 10;//No se puede referenciar desde un contexto estático
        Ejercicio_con_contexto_estatico_8_7 personaP1 = new Ejercicio_con_contexto_estatico_8_7();
        System.out.println(personaP1.getContador());
    }

    static public void imprimir(Contexto_estatico_práctica_Parte_1_8_5 persona) {
        System.out.println("persona = " + persona);
    }

    public int getContador() {
        imprimir(new Contexto_estatico_práctica_Parte_1_8_5("Liliana"));
        return this.contador;
    }
}
