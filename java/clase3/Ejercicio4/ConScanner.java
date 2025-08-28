import java.util.Scanner;


/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo,
y mostrar cuántos números se han introducido.
Lo haremos con la clase Scanner
Luego con la Clase JOptionPane
*/
public class ConScanner {
    public static void main(String[] args) {
        int contador = 0;
        int num;
        Scanner sc = new Scanner(System.in);

        do {
            System.out.println("Introduce un numero");
            num = sc.nextInt();
            contador++;
        } while (num >= 0);
        System.out.println("Has introducido " + contador + " números, uno negativo");
        
    }
}
