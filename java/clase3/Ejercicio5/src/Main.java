import java.util.Random;
import java.util.Scanner;

/**
 * Ejercicio 5: Realizar un juego para adivinar un número para ello
 * generar un número aleatorio entre 0-100, y luego ir pidiendo números
 * indicando "es mayor" o "es menor" según sea mayor o menor con respecto
 * a N.
 * El proceso termina cuando el usuario acierta y mostramos el número de intentos hechos
 */
public class Main {
    public static void main(String[] args) {
        Random rnd = new Random();
        int userNumber;
        int secretNumber;
        int attempts = 0;
        boolean foundSecretNumber = false;

        System.out.println("""
                Bienvenido al juego de adivinanza de números
                Tendrás que elegir del 0 al 100 el número correcto
                El sistema te irá indicando si el número es mayor o menor
                según el número secreto.
                """);

        secretNumber = rnd.nextInt(0, 100);

        while(!foundSecretNumber){
            System.out.println("Ingresa el número que crees que es el correcto");
            userNumber = getUserNumber();
            attempts++;
            if(secretNumber > userNumber) System.out.println("El número secreto es mayor");
            if(secretNumber < userNumber) System.out.println("El número secreto es menor");
            if(userNumber == secretNumber) foundSecretNumber = true;
        }
        System.out.printf("El juego ha finalizado el número correcto era %s, en %d intentos", secretNumber, attempts);
    }

    private static int getUserNumber(){
        Scanner sc = new Scanner(System.in);
        return sc.nextInt();
    }
}