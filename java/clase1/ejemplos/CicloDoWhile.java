package clase1.ejemplos;

class CicloDoWhile {
    public static void main(String[] args) {
        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;
        } while (contador <= 7);
    }
}
