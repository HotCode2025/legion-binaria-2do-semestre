public class PruebaAritmetica {

    void main() {
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();

        int resultado = aritmetica1.sumarConRetorno();
        IO.println("resultado = " + resultado);

        resultado = aritmetica1.sumarConArgumentos(12, 26);
        IO.println("Resultado usando argumentos = " + resultado);
    }

    class Aritmetica {
        //Atributos de la clase

        int a;
        int b;

        //Metodo
        public void sumarNumeros() {
            int resultado = a + b;
            IO.println("Resultado= " + resultado);
        }

        public int sumarConRetorno() {
            // int resultado = a + b;
            return a + b;
        }

        public int sumarConArgumentos(int arg1, int arg2){
            a = arg1;
            b = arg2;
            //return a+b;
            return sumarConRetorno();
        }


    }
}
