public class Labels {
    // Uso de las palabras break y continue junto a las etiquetas (labels)    
    public static void main(String[] args) {
        inicio:
        for (int contando = 0; contando < 7; contando++) {
            if (contando % 2 == 0) {
                System.out.println("contando = " + contando);
                break inicio;
            }
        }
        //
        System.out.println("//--//--//--//--//--//--//--//--//");
        //
        inicio:
        for(int contando = 0; contando < 7; contando++){
            if(contando % 2 != 0){
                continue inicio;
            }
            System.out.println("contando = " + contando);
        }
    }
}