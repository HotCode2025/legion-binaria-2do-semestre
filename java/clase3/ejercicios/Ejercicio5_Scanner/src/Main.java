import java.util.Random;
import java.util.Scanner;

/**
 * Ejercicio 5: Realizar un juego para adivinar un número para ello
 * generar un número aleatorio entre 0-100, y luego ir pidiendo números
 * indicando "es mayor" o "es menor" según sea mayor o menor con respecto
 * a N.
 * El proceso termina cuando el usuario acierta y mostramos el número de
 * intentos hechos
 */
public class Main {
    public static void main(String[] args) {
        final int MAX_VALUE = 100;
        int attempts = 0;
        int userNumber;

        Random random = new Random();
        int secret = random.nextInt(MAX_VALUE + 1);

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Adivina el número entre 0 y 100");

            do {
                System.out.print("Ingresa tu número: ");

                while (!scanner.hasNextInt()) {
                    System.out.print("Entrada inválida. Ingresa un número entero: ");
                    scanner.next();
                }
                userNumber = scanner.nextInt();
                attempts++;
                if (userNumber < secret) {
                    System.out.println("El número secreto es mayor");
                } else if (userNumber > secret) {
                    System.out.println("El número secreto es menor");
                } else {
                    System.out.printf("El juego ha finalizado el número correcto era %d. Intentos: %d%n", secret, attempts);
                }
            } while (userNumber != secret);
        }
    }
}
