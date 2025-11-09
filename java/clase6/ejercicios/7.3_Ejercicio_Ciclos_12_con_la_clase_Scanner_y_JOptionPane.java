import java.util.Scanner;
import javax.swing.JOptionPane;

public class Factorial {
    public static void main(String[] args) {
        // Usando Scanner
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese un número para calcular su factorial: ");
        int numero1 = sc.nextInt();
        System.out.println("El factorial de "+numero1+" es: "+factorial(numero1));

        // Usando JOptionPane
        String input = JOptionPane.showInputDialog("Ingrese un número para calcular su factorial: ");
        int numero2 = Integer.parseInt(input);
        JOptionPane.showMessageDialog(null, "El factorial de "+numero2+" es: "+factorial(numero2));
    }

    // Método factorial (iterativo)
    public static long factorial(int n) {
        long resultado = 1;
        for (int i = 1; i <= n; i++) {
            resultado *= i;
        }
        return resultado;
    }
}