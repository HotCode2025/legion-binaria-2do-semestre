import javax.swing.JOptionPane;

/**
 * Ejercicio 3: Leer números hasta que se introduzca un cero
 * Para cada uno indicar si es par o impar.
 * Primero lo haremos con la clase Scanner
 * Luego con la Clase JOptionPane
 */

public class Main2 {
    public static void main(String[] args) {
        int numero;
        do {
            String input = JOptionPane.showInputDialog(null, "Introduce un numero (0 para salir):");

            if (input == null) {
                // Si el usuario cierra la ventana se corta el bucle
                break;
            }

            numero = Integer.parseInt(input);

            if (numero != 0) {
                if (numero % 2 == 0) {
                    JOptionPane.showMessageDialog(null, numero + " es par");
                } else {
                    JOptionPane.showMessageDialog(null, numero + " es impar");
                }
            }
        } while (numero != 0);

        JOptionPane.showMessageDialog(null, "Programa finalizado.");
    }
}
