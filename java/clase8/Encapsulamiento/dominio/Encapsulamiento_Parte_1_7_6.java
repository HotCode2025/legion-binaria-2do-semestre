
package dominio;

public class Encapsulamiento_Parte_1_7_6 {
    //Atributos
    String nombre;
    private double sueldo;
    private boolean eliminado;
    
    //Constructor
    public Encapsulamiento_Parte_1_7_6(String nombre, double sueldo, boolean eliminado){
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }

    public Encapsulamiento_Parte_1_7_6(String osvaldo) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    public Encapsulamiento_Parte_1_7_6() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    
    public String toString(){ //Convierte en una cadena atributo
        return "Persona [ nombre: " + this.nombre + 
                ", sueldo: " + this.sueldo +
                ", eliminado: " + this.eliminado + " ]";
    }
}
