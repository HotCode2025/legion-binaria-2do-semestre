public class Ejemplo5_1CreandoUnObjeto {
    public static void main(String[] args) {
        Aritmetica aritmetica = new Aritmetica();
        aritmetica.a = 10;
        aritmetica.b = 20;
        aritmetica.sumarNumeros();
    }
}

class Aritmetica {
    public int a;
    public int b;

    public void sumarNumeros() {
        System.out.println("Resultado: " + (a + b));
    }
}