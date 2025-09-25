
package Clases;

import javax.swing.JOptionPane;

public class Clase6_Ciclos {
     public static void main(String[] args) {
        long producto = 1; // usamos long porque el resultado puede ser muy grande

        for (int i = 1; i <= 10; i++) {
            int numero;

            // Bucle para asegurarnos de que el número sea impar
            while (true) {
                String input = JOptionPane.showInputDialog("Ingresa el número impar " + i + ":");
                
                try {
                    numero = Integer.parseInt(input);

                    if (numero % 2 != 0) { // condición de impar
                        break;
                    } else {
                        JOptionPane.showMessageDialog(null, 
                            "El número ingresado no es impar. Intenta de nuevo.");
                    }
                } catch (NumberFormatException e) {
                    JOptionPane.showMessageDialog(null, 
                        "Entrada inválida. Ingresa un número entero.");
                }
            }

            producto *= numero;
        }

        JOptionPane.showMessageDialog(null, 
            "El producto de los 10 números impares ingresados es: " + producto);
    }
}
