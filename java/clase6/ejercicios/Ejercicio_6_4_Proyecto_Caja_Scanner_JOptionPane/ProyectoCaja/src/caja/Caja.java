package caja;
public class Caja {
    private double ancho;
    private double alto;
    private double profundidad;
    //vacío
    public Caja() {
        this.ancho = 0;
        this.alto = 0;
        this.profundidad = 0;
    }
    //con parámetros
    public Caja(double ancho, double alto, double profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }
    public double calcularVolumen() {
        return ancho * alto * profundidad;
    }
    public void mostrarDimensiones() {
        System.out.println("Ancho: " + ancho);
        System.out.println("Alto: " + alto);
        System.out.println("Profundidad: " + profundidad);
    }
}