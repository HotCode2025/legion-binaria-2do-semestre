
package test;

import operaciones.Sobrecarga_de_Métodos_10_2;

public class Sobrecarga_de_Métodos_10_2_Test {
    public static void main(String[] args) {
        var resultado = Sobrecarga_de_Métodos_10_2.sumar(7, 9);
        System.out.println("resultado = " + resultado);
        
        var resultado2 = Sobrecarga_de_Métodos_10_2.sumar(5.0, 7);
        System.out.println("resultado2 = " + resultado2);
        
        var resultado3 = Sobrecarga_de_Métodos_10_2.sumar(8, 6L);
        System.out.println("resultado3 = " + resultado3);
    }
}
