
public class Clase5 {
    
    int a;
    int b;

    // Método
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }

    public int sumarConRetorno() {
        // int resultado = a + b;
        return this.a + this.b;
    }
    
    //Operador this

    public int sumarConArgumentos(int a, int b) {
        this.a = a; // El argumento a se asigna al atributo this.a
        this.b = b;
        // return a + b;
        return this.sumarConRetorno();
    }
}


