package app;

import java.sql.Date;

public class Cliente {
    private static int contador = 0;
    private int idCliente;
    private Date fechaRegistro;
    private boolean vip;

    public Cliente() {
    }

    public Cliente(Date fechaRegistro, boolean vip) {
        this.idCliente = contador++;
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
    }

    public int getId() {
        return idCliente;
    }

    public Date getFechaRegistro() {
        return fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean idVip() {
        return vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }

    public int getIdCliente() {
        return idCliente;
    }

    @Override
    public String toString() {
        return "Cliente [idCliente=" + idCliente + ", fechaRegistro=" + fechaRegistro + ", vip=" + vip + "]";
    }
}
