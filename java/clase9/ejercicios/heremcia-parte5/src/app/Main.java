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
    }
}
