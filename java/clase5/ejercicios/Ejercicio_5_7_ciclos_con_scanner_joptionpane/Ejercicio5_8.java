import java.util.Scanner;
import javax.swing.JOptionPane;

/*
Ejercicio 9: Pedir el día, mes y año de una fecha e
indicara si la fecha es correcta. Suponiendo que 
todos los meses son de 30 días
*/

public class Ejercicio5_8{
    public static void main(String[] args) {
        // Versión con Scanner
        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese el día: ");
        int dia = sc.nextInt();

        System.out.print("Ingrese el mes: ");
        int mes = sc.nextInt();

        System.out.print("Ingrese el año: ");
        int año = sc.nextInt();

        if (dia >= 1 && dia <= 30 && mes >= 1 && mes <= 12 && año > 0) {
            System.out.println("La fecha es CORRECTA: " + dia + "/" + mes + "/" + año);
        } else {
            System.out.println("La fecha es INCORRECTA.");
        }

        
        // Versión con JOptionPane
       

        int dia2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el día:"));
        int mes2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes:"));
        int año2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año:"));

        if (dia2 >= 1 && dia2 <= 30 && mes2 >= 1 && mes2 <= 12 && año2 > 0) {
            JOptionPane.showMessageDialog(null, 
                "La fecha es CORRECTA: " + dia2 + "/" + mes2 + "/" + año2);
        } else {
            JOptionPane.showMessageDialog(null, "La fecha es INCORRECTA.");
        }

        sc.close();
    }
}