
package domain;

public class Agregamos_el_toString_11_5 {
    private String nombre;

    public Agregamos_el_toString_11_5(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Agregamos_el_toString_11_5{" + "nombre=" + nombre + '}'+", "+super.toString();
    }
    
    
    
}
