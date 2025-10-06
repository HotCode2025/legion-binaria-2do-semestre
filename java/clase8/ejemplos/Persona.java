package clase8.ejemplos;


public class Persona {
    // Cargamos los atributos
    private int idPersona;
    private static int contadorPersona;
    private String nombre;

    // Constructor
    public Persona(String nombre) {
        this.nombre = nombre;
        // Incrementar el contador por cada objeto nuevo
        Persona.contadorPersona++; // No utilizar el operador this
        // Vamos a asignar un nuevo valor a la variable idPersona
        this.idPersona =Persona.contadorPersona;
    }

    // Métodos get y set para contadorPersona
    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int aContadorPersona) {
        contadorPersona = aContadorPersona;
    }

    // Sobrescribir método toString
    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
}
