package app;

import java.sql.Date;

public class Main {
    public static void main(String[] args) {
        // crear tres clases clientes usando la fecha actual con Date
        Cliente c1 = new Cliente(new Date(System.currentTimeMillis()), true);
        Cliente c2 = new Cliente(new Date(System.currentTimeMillis()), false);
        Cliente c3 = new Cliente(new Date(System.currentTimeMillis()), true);
        System.out.println(c1);
        System.out.println(c2);
        System.out.println(c3);

        // crear tres clases empleados
        Empleado e1 = new Empleado(1233);
        Empleado e2 = new Empleado(2344);
        Empleado e3 = new Empleado(3455);
        System.out.println(e1);
        System.out.println(e2);
        System.out.println(e3);
    }
}
