
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.Orden_Comenzamos_con_la_clase_Orden_Parte_3_13_6;
import ar.com.codesystem.ventas.Producto_13_2_Creamos_la_clase_Producto;


public class Ahora_vamos_a_hacer_una_tarea_con_Diseño_de_clase_13_8 {
    public static void main(String[] args) {
        Producto_13_2_Creamos_la_clase_Producto producto1 = new Producto_13_2_Creamos_la_clase_Producto(" Pantalon", 9500.00);
        Producto_13_2_Creamos_la_clase_Producto producto2 = new Producto_13_2_Creamos_la_clase_Producto(" Campera", 29900.00);
        Producto_13_2_Creamos_la_clase_Producto producto3 = new Producto_13_2_Creamos_la_clase_Producto(" Zapatillas", 290900.00);
        Producto_13_2_Creamos_la_clase_Producto producto4 = new Producto_13_2_Creamos_la_clase_Producto(" Remera", 19900.00);
        Producto_13_2_Creamos_la_clase_Producto producto5 = new Producto_13_2_Creamos_la_clase_Producto(" Medias", 1900.00);
        Producto_13_2_Creamos_la_clase_Producto producto6 = new Producto_13_2_Creamos_la_clase_Producto(" Mochila", 55500.00);
        Producto_13_2_Creamos_la_clase_Producto producto7 = new Producto_13_2_Creamos_la_clase_Producto(" Shorts", 15000.00);
        Producto_13_2_Creamos_la_clase_Producto producto8 = new Producto_13_2_Creamos_la_clase_Producto(" Botines", 290900.00);
        Producto_13_2_Creamos_la_clase_Producto producto9 = new Producto_13_2_Creamos_la_clase_Producto(" Botas", 199900.00);
        Producto_13_2_Creamos_la_clase_Producto producto10 = new Producto_13_2_Creamos_la_clase_Producto(" Pelota de futbol", 6900.00);
        
        Orden_Comenzamos_con_la_clase_Orden_Parte_3_13_6 orden1 = new Orden_Comenzamos_con_la_clase_Orden_Parte_3_13_6();
        Orden_Comenzamos_con_la_clase_Orden_Parte_3_13_6 orden2 = new Orden_Comenzamos_con_la_clase_Orden_Parte_3_13_6();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto6);
        orden2.agregarProducto(producto7);
        orden2.agregarProducto(producto8);
        orden2.agregarProducto(producto9);
        orden2.agregarProducto(producto10);
        
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        
        
        //Tarea:
        //Crear mas objetos de tipo Producto = 10
        //Crear mas objetos de tipo Orden = 2
        
    }
}
