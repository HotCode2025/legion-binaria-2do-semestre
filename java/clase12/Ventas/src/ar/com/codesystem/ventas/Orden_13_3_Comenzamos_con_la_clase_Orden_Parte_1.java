
package ar.com.codesystem.ventas;

public class Orden_13_3_Comenzamos_con_la_clase_Orden_Parte_1 {
    private int idOrden;
    private Producto_13_2_Creamos_la_clase_Producto productos[]; //Declaramos el arreglo
    static int contadorOrdenes;
    private int contadorProductos;
    static final int MAX_PRODUCTOS = 10;
    
    //Constructor vacio
    public Orden_13_3_Comenzamos_con_la_clase_Orden_Parte_1(){
        this.idOrden = ++Orden_13_3_Comenzamos_con_la_clase_Orden_Parte_1.contadorOrdenes;
        this.productos = new Producto_13_2_Creamos_la_clase_Producto[Orden_13_3_Comenzamos_con_la_clase_Orden_Parte_1.MAX_PRODUCTOS];
    }
    
    public void agregarProducto(Producto_13_2_Creamos_la_clase_Producto producto){
        if(this.contadorProductos < Orden_13_3_Comenzamos_con_la_clase_Orden_Parte_1.MAX_PRODUCTOS){
            this.productos[this.contadorProductos++] = producto;
        }
        else{
            System.out.println("Se ha superado el maximo de productos: "+Orden_13_3_Comenzamos_con_la_clase_Orden_Parte_1.MAX_PRODUCTOS);
        }
    }
}
