
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.Orden_Comenzamos_con_la_clase_Orden_Parte_3_13_6;
import ar.com.codesystem.ventas.Producto_13_2_Creamos_la_clase_Producto;

public class VentasTest_Comenzamos_con_las_pruebas_en_VentasTest_13_7 {
    public static void main(String[] args) {
        Producto_13_2_Creamos_la_clase_Producto producto1 = new Producto_13_2_Creamos_la_clase_Producto("Pantalon ", 9500.00);
        Producto_13_2_Creamos_la_clase_Producto producto2 = new Producto_13_2_Creamos_la_clase_Producto("Campera ", 29900.00);
        
        
        Orden_Comenzamos_con_la_clase_Orden_Parte_3_13_6 orden1 = new Orden_Comenzamos_con_la_clase_Orden_Parte_3_13_6();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
       
        
        orden1.mostrarOrden();
        
        
        //Tarea:
        //Crear mas objetos de tipo Producto = 10
        //Crear mas objetos de tipo Orden = 2
    }
}
