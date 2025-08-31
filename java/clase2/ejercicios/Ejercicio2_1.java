package clase2.ejercicios;

import javax.swing.JOptionPane;

/* 
 * Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el proceso hasta que se introduzca un numero negativo
 */
public class Ejercicio2_1 {
    public static void main(String[] args) {
        int numero, cuadrado;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
        while (numero >= 0) {
            cuadrado = (int) Math.pow(numero, 2);
            System.out.println("El número " + numero + " elevado al cuadrado es : " + cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
        }
        System.out.println("El programa a finalizado por numero negativo");
    }
}
