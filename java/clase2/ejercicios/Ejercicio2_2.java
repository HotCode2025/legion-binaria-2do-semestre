package clase2.ejercicios;

import java.util.Scanner;
import javax.swing.JOptionPane;
    
/* 
 * Leer un número e indicar si es positivo o negativo. El proceso  
 * se repetira hasta que se introduzca un cero. 
 */
public class Ejercicio2_2 {
    public static void main(String[] args) {
        // Ejercicio 2 con la clase scanner
        Scanner sc = new Scanner(System.in);
        int num;
        do {
            System.out.println("Introduce un numero");
            num = sc.nextInt();
            if (num > 0) {
                System.out.println(num + " es positivo");
            } else if (num < 0) {
                System.out.println(num + " es negativo");
            }
        } while (num != 0);
        System.out.println("Programa finalizado.");
        sc.close();

        // Ejercicio 2 con la clase JOptionPane
        int num2;
        do {
            num2 = Integer.parseInt(JOptionPane.showInputDialog("Introduce un numero"));
            if (num2 > 0) {
                JOptionPane.showMessageDialog(null, num2 + " es positivo");
            } else if (num2 < 0) {
                JOptionPane.showMessageDialog(null, num2 + " es negativo");
            }
        } while (num2 != 0);
        JOptionPane.showMessageDialog(null, "Programa finalizado.");
    }
}
