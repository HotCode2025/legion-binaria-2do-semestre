
package ar.com.codesystem.ventas;


public class Comenzamos_con_la_clase_Orden_Parte_3_13_5 {
    private int idOrden;
    private Producto_13_2_Creamos_la_clase_Producto productos[]; //Declaramos el arreglo
    static int contadorOrdenes;
    private int contadorProductos;
    static final int MAX_PRODUCTOS = 10;
    
    //Constructor vacio
    public Comenzamos_con_la_clase_Orden_Parte_3_13_5(){
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
    
    public double calcularTotal(){
        double total = 0; //Variable temporal
        for(int i = 0; i < this.contadorProductos; i++) {
            //Producto_13_2_Creamos_la_clase_Producto producto = this.productos[i];
            //total += producto.getPrecio();
            total += this.productos[i].getPrecio();
        }
        return total;
    }
}