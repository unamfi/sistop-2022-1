package mx.unam.sistop.proyecto1.utilidades;

/**
 * Acumulador thread-safe.
 */
public class AcumuladorSeguro {
    private int valor = 0;

    /**
     * Se utiliza el patrón de diseño de monitor soportado por Java donde, al llamarse este método, se adquiere el Lock
     * de este objeto, y al terminar su ejecución se libera. Lo anterior hace posible que la operación se lleve a cabo
     * de forma atómica.
     *
     * @return Nuevo valor
     */
    public synchronized int incrementarYObtener() {
        return ++valor;
    }
}
