import javax.swing.JOptionPane;

public class ConJOptionPane {
    public static void main(String[] args) {
        int contador = 0;
        int num;
        do {
            num = Integer.parseInt(JOptionPane.showInputDialog("Introduce un numero"));
            contador++;
        } while (num >= 0);
        JOptionPane.showMessageDialog(null, "Has introducido " + contador + " numeros, uno negativo");
    }
}