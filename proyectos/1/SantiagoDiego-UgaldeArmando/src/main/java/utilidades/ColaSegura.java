package utilidades;

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * Cola thread-safe. Para su implementación se utilizaron dos semáforos: vacíos y llenos. Estos permiten que se logren
 * encolar y desencolar elementos siempre y cuando haya lugares disponibles o haya elementos en la cola,
 * respectivamente. En caso de que la condición deseada no se cumpla, el llamador será bloqueado hasta que sea posible
 * realizar la operación. De igual forma, se utilizó un Lock en la cola interna para que esta únicamente se modifique de
 * forma atómica.
 *
 * @param <T> Tipo de elementos a contener.
 */
public class ColaSegura<T> {
    private final Semaphore vacios;
    private final Semaphore llenos;
    private final Lock lockDeCola = new ReentrantLock();
    private final Queue<T> cola;

    public ColaSegura(int maximaCapacidad) {
        // Todos los espacios de la cola están vacíos inicialmente.
        this.vacios = new Semaphore(maximaCapacidad);
        // No hay ningún espacio lleno inicialmente.
        this.llenos = new Semaphore(0);
        this.cola = new ArrayDeque<>();
    }

    public void encolar(T elemento) {
        try {
            // Solo se puede encolar un elemento si hay un espacio vacío.
            vacios.acquire();
        } catch (InterruptedException e) {
            e.printStackTrace();
            throw new RuntimeException("EL HILO FUE INTERRUMPIDO AL ENCOLAR");
        }

        // Encolar el elemento en la cola interna de forma atómica.
        lockDeCola.lock();
        cola.add(elemento);
        lockDeCola.unlock();

        // Ahora hay otro espacio lleno.
        llenos.release();
    }

    public T desencolar() {
        T desencolado;
        try {
            // Solo se puede desencolar un elemento si hay un elemento al menos.
            llenos.acquire();
        } catch (InterruptedException e) {
            e.printStackTrace();
            throw new RuntimeException("EL HILO FUE INTERRUMPIDO AL DESENCOLAR");
        }

        // Desencolar el elemento en la cola interna de forma atómica.
        lockDeCola.lock();
        desencolado = cola.remove();
        lockDeCola.unlock();

        // Ahora hay otro espacio vacío.
        vacios.release();
        return desencolado;
    }
}
