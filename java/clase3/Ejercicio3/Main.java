
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero;

        do {
            System.out.print("Introduce un numero (0 para salir): ");
            numero = sc.nextInt();

            if (numero != 0) {
                if (numero % 2 == 0) {
                    System.out.println(numero + " es par");
                } else {
                    System.out.println(numero + " es impar");
                }
            }
        } while (numero != 0);

        System.out.println("Programa finalizado.");
        sc.close();
    }
}
