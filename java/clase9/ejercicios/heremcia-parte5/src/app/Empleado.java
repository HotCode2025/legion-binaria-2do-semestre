package app;

public class Empleado {
    private static int contador = 0;
    private int idEmpleado;
    private double sueldo;

    public Empleado() {
    }

    public Empleado(double sueldo) {
        this.idEmpleado = contador++;
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return idEmpleado;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        return "Empleado [idEmpleado=" + idEmpleado + ", sueldo=" + sueldo + "]";
    }
}
