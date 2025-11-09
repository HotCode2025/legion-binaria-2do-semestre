import java.util.Scanner;
import javax.swing.JOptionPane;
public class SumaNumeros {
    public static void main(String[] args) {
        //consola con scanner
        Scanner scanner = new Scanner(System.in);
        double sumaConsola = 0;
        System.out.println("Ingresar los 10 numeros para sumar:");
        for (int i = 1; i <= 10; i++) {
            System.out.print("Número " + i + ": ");
            double num = scanner.nextDouble();
            sumaConsola += num;
        }
        System.out.println("La suma es: " + sumaConsola);
        //joptionpane
        double sumaJOP = 0;
        System.out.println("\nPor JOptionPane:");
        for (int i = 1; i <= 10; i++) {
            String input = JOptionPane.showInputDialog("Ingrese el número " + i + ":");
            double num = Double.parseDouble(input);
            sumaJOP += num;
        }
        JOptionPane.showMessageDialog(null, "La suma es: " + sumaJOP);
    }
}