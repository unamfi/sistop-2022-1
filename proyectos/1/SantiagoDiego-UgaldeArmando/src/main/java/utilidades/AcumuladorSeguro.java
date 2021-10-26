package utilidades;

public class AcumuladorSeguro {
    private int valor = 0;

    public synchronized int incrementarYObtener() {
        return ++valor;
    }
}
