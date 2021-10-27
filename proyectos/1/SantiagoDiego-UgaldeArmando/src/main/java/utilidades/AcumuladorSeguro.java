package utilidades;

/**
 * Acumulador thread-safe.
 */
public class AcumuladorSeguro {
    private int valor = 0;

    public synchronized int incrementarYObtener() {
        return ++valor;
    }
}
