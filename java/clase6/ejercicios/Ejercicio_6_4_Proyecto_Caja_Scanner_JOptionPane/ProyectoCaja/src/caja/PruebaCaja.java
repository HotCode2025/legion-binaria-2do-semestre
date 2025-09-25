package caja;
import java.util.Scanner;
import javax.swing.JOptionPane;
public class PruebaCaja {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        //constructor vacío
        Caja cajaVacia = new Caja();
        System.out.println("Constructor vacío:");
        cajaVacia.mostrarDimensiones();
        System.out.println("Volumen: " + cajaVacia.calcularVolumen());
        //consola
        System.out.println("\n--- Ingresar por consola ---");
        System.out.print("Ancho: ");
        double anchoConsola = scanner.nextDouble();
        System.out.print("Alto: ");
        double altoConsola = scanner.nextDouble();
        System.out.print("Profundidad: ");
        double profundidadConsola = scanner.nextDouble();
        Caja cajaConsola = new Caja(anchoConsola, altoConsola, profundidadConsola);
        System.out.println("\nResultado:");
        cajaConsola.mostrarDimensiones();
        System.out.println("Volumen: " + cajaConsola.calcularVolumen());
        // 🔹 Entrada por JOptionPane
        System.out.println("\n--- Ingresar por JOptionPane ---");
        double anchoJOP = Double.parseDouble(JOptionPane.showInputDialog("Ancho:"));
        double altoJOP = Double.parseDouble(JOptionPane.showInputDialog("Alto:"));
        double profundidadJOP = Double.parseDouble(JOptionPane.showInputDialog("Profundidad:"));
        Caja cajaJOP = new Caja(anchoJOP, altoJOP, profundidadJOP);
        JOptionPane.showMessageDialog(null,
            "Resultado:\n" +
            "Ancho: " + anchoJOP + "\n" +
            "Alto: " + altoJOP + "\n" +
            "Profundidad: " + profundidadJOP + "\n" +
            "Volumen: " + cajaJOP.calcularVolumen()
        );
    }
}