
package domain;

public class Contexto_estatico_práctica_Parte_1_8_5 {

    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int aContadorPersona) {
        contadorPersona = aContadorPersona;
    }
    
    //Cargamos los atributos
    private int idPersona;
    private static int contadorPersona;
    private String nombre;
    
    //Constructor
    public Contexto_estatico_práctica_Parte_1_8_5(String nombre){
        this.nombre = nombre;
        //Incrementar el contador por cada objeto nuevo
        Contexto_estatico_práctica_Parte_1_8_5.contadorPersona++; // No utilizar el operador this
        //Vamos a asignar un nuevo valor a la variedad idPersonal
        this.idPersona = Contexto_estatico_práctica_Parte_1_8_5.contadorPersona;
    }

    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
       @Override
    public String toString() {
        return "Contexto_estatico_pr\u00e1ctica_Parte_1_8_5{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
}
