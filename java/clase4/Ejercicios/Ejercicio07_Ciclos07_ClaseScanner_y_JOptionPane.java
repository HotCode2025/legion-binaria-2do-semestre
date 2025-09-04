import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio_07 {

    // Metodo con Scanner
    public static void usarScanner() {
        Scanner entrada = new Scanner(System.in);

        int numero;
        int suma = 0;
        int contador = 0;

        System.out.println("Ingrese un número positivo (negativo para salir): ");
        numero = entrada.nextInt();

        while (numero >= 0) {
            suma += numero;
            contador++;
            System.out.println("Ingrese otro número positivo (negativo para salir): ");
            numero = entrada.nextInt();
        }

        if (contador == 0) {
            System.out.println("No ingresaste ningún número válido.");
        } else {
            double media = (double) suma / contador; // Calculamos la media
            System.out.println("La media de los números es: " + media);
        }
    }

    // Metodo con JOptionPane
    public static void usarJOptionPane() {
        int numero;
        int suma = 0;
        int contador = 0;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número positivo (negativo para salir):"));

        while (numero >= 0) {
            suma += numero;
            contador++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número positivo (negativo para salir):"));
        }

        if (contador == 0) {
            JOptionPane.showMessageDialog(null, "No ingresaste ningún número válido.");
        } else {
            double media = (double) suma / contador;
            JOptionPane.showMessageDialog(null, "La media de los números es: " + media);
        }
    }

    // Metodo principal
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        // Menu con un booleano para elegir el metodo. (true=Scanner, false= JOptionPane)
        System.out.println("¿Quieres usar Scanner (true) o JOptionPane (false)?");
        boolean usarScanner = entrada.nextBoolean();

        if (usarScanner) {
            usarScanner();
        } else {
            usarJOptionPane();
        }
    }
}
