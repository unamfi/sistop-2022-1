package utilidades;

import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * Conjunto thread-safe. Para su implementación se utilizó un semáforo: vacíos. Éste permite que se agreguen elementos
 * al conjunto interno sólo si hay suficiente espacio. De lo contrario, el llamador se bloqueará hasta que se cumpla la
 * condición anterior. De igual forma, se utilizó un Lock en el conjunto interno para que las operaciones ejecutadas en
 * eśte se realicen de forma atómica, previniendo así posibles condiciones de carrera.
 *
 * @param <T> Tipo de elementos a contener.
 */
public class ConjuntoSeguro<T> {
    private final Semaphore vacios;
    private final Lock lockDeConjunto = new ReentrantLock();
    private final Set<T> conjunto;

    public ConjuntoSeguro(int maximaCapacidad) {
        // Inicialmente todos los espacios están vacíos.
        this.vacios = new Semaphore(maximaCapacidad);
        this.conjunto = new HashSet<>();
    }

    public void agregar(T elemento) {
        try {
            // Solo se puede agregar un elemento si hay un espacio vacío al menos.
            vacios.acquire();
        } catch (InterruptedException e) {
            e.printStackTrace();
            throw new RuntimeException("EL HILO FUE INTERRUMPIDO AL AGREGAR");
        }

        // Agregar elemento de forma atómica
        lockDeConjunto.lock();
        conjunto.add(elemento);
        lockDeConjunto.unlock();
    }

    public void eliminar(T elemento) {
        // Eliminar elemento de forma atómica.
        lockDeConjunto.lock();
        if (!conjunto.contains(elemento)) throw new RuntimeException("EL CONJUNTO NO CONTIENE EL ELEMENTO DESEADO");
        conjunto.remove(elemento);
        lockDeConjunto.unlock();

        // Ahora hay un espacio vacío más.
        vacios.release();
    }
}
