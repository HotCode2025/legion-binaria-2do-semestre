import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio5_7 {
    public static void main(String[] args) {

        // Pedir número con Scanner
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese un número entero por consola: ");
        int numsc = scanner.nextInt();
        System.out.println("Números del 1 al " + numsc + ":");
        for (int i = 1; i <= numsc; i++) {
            System.out.print(i + " ");
        }
        scanner.close();

        System.out.println("\n-----------------------------");

        // Pedir número con JOptionPane
        String input = JOptionPane.showInputDialog("Ingrese un número entero:");
        int npane = Integer.parseInt(input);

        StringBuilder resultado = new StringBuilder("Números del 1 al " + npane + ":\n");
        for (int i = 1; i <= npane; i++) {
            resultado.append(i).append(" ");
        }
        JOptionPane.showMessageDialog(null, resultado.toString());
    }
}