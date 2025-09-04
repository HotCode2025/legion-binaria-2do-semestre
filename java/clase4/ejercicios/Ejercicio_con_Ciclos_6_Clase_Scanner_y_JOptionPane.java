import java.util.Scanner;
import javax.swing.JOptionPane;
public class Ejercicio_con_Ciclos_6_Clase_Scanner_y_JOptionPane {
    public static void main(String[] args) {
        int sumajo = 0;
        int numerojo;
        do {
            String input = JOptionPane.showInputDialog("Ingrese numero (0 para terminar):");
            if (input == null) {
                JOptionPane.showMessageDialog(null, "Cancelado.");
                break;
            }
            numerojo = Integer.parseInt(input);
            sumajo += numerojo;
        } while (numerojo != 0);
        JOptionPane.showMessageDialog(null, "La suma de lo ingresado es: " + sumajo);

        //--------------------//

        Scanner scanner = new Scanner(System.in);
        int sumasc = 0;
        int numerosc;
        System.out.println("Ingrese números. 0 para terminar:");
        do {
            System.out.print("Número: ");
            numerosc = scanner.nextInt();
            sumasc += numerosc;
        } while (numerosc != 0);
        System.out.println("La suma de lo ingresado es: " + sumasc);
        scanner.close();    
    }
}

