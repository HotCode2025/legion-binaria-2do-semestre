
package test;

import domain.Contexto_estatico_práctica_Parte_1_8_5;

public class Contexto_estático_práctica_Parte_2_Ejecutar_con_debug_File_8_6 {
    private int contador;

    public static void main(String[] args) {
        Contexto_estatico_práctica_Parte_1_8_5 persona1 = new Contexto_estatico_práctica_Parte_1_8_5("Ariel");
        System.out.println("persona1 = " + persona1);
        Contexto_estatico_práctica_Parte_1_8_5 persona2 = new Contexto_estatico_práctica_Parte_1_8_5("Naty");
        System.out.println("persona2 = " + persona2);
        imprimir(persona1);
        imprimir(persona2);
        // this.contador = 10; //No se puede referenciar desde un contexto éstatico
        Contexto_estático_práctica_Parte_2_Ejecutar_con_debug_File_8_6 obj = new Contexto_estático_práctica_Parte_2_Ejecutar_con_debug_File_8_6();
        System.out.println(obj.getContador());
    }

    static public void imprimir(Contexto_estatico_práctica_Parte_1_8_5 persona) {
        System.out.println("persona = " + persona);
    }

    public int getContador() {
        imprimir(new Contexto_estatico_práctica_Parte_1_8_5("Liliana"));
        return this.contador;
    }
}
