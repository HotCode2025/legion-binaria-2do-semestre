
package ar.com.codesystem.ventas;

public class Producto_13_2_Creamos_la_clase_Producto {
    //Atributos de la clase
    private int idProducto;
    private String nombre;
    private double precio;
    private static int contadorProductos;
    
    
    //Constructor vacio
    private Producto_13_2_Creamos_la_clase_Producto(){
        this.idProducto = ++Producto_13_2_Creamos_la_clase_Producto.contadorProductos;
    }
    
    public Producto_13_2_Creamos_la_clase_Producto(String nombre, double precio){
        this(); //Llamamos al constructor vacio para el aumento de idProducto
        this.nombre = nombre;
        this.precio = precio;
    }

    public int getIdProducto() {
        return idProducto;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    @Override
    public String toString() {
        return "Producto_13_2_Creamos_la_clase_Producto{" + "idProducto=" + idProducto + ", nombre=" + nombre + ", precio=" + precio + '}';
    }
    
    
    
    
    
}
