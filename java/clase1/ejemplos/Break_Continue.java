package clase1.ejemplos;

public class Break_Continue {
    public static void main(String[] args) {        
        // Uso de las palabras break y continue       
        for(var contando = 0; contando < 7; contando++ ){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break;
            }
        }
        for(var contando = 0; contando < 7; contando++ ){
            if(contando % 2 != 0){
                continue;
            }
            System.out.println("contando = " + contando);
        }        
    }
}
