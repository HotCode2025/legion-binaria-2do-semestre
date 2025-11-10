
package ar.com.codesystem.ventas;

public class Comenzamos_con_la_clase_Orden_Parte_2_13_4 {
    private int idOrden;
    private Producto_13_2_Creamos_la_clase_Producto productos[]; //Declaramos el arreglo
    private static int contadorOrdenes;
    private int contadorProductos;
    private static final int MAX_PRODUCTOS = 10;
    
    //Constructor vacio
    public Comenzamos_con_la_clase_Orden_Parte_2_13_4(){
        this.idOrden = ++Orden_13_3_Comenzamos_con_la_clase_Orden_Parte_1.contadorOrdenes;
        this.productos = new Producto_13_2_Creamos_la_clase_Producto[Orden_13_3_Comenzamos_con_la_clase_Orden_Parte_1.MAX_PRODUCTOS];
    }
    
}
