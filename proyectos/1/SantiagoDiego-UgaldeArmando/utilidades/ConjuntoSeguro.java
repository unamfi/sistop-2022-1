package utilidades;

import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ConjuntoSeguro<T> {
    private final Semaphore vacios;
    private final Lock lockDeConjunto = new ReentrantLock();
    private final Set<T> conjunto;

    public ConjuntoSeguro(int maximaCapacidad) {
        this.vacios = new Semaphore(maximaCapacidad);
        this.conjunto = new HashSet<>();
    }

    public void agregar(T elemento) {
        try {
            vacios.acquire();
        } catch (InterruptedException e) {
            e.printStackTrace();
            throw new RuntimeException("EL HILO FUE INTERRUMPIDO AL AGREGAR");
        }

        lockDeConjunto.lock();
        conjunto.add(elemento);
        lockDeConjunto.unlock();
    }

    public void eliminar(T elemento) {
        lockDeConjunto.lock();
        if (!conjunto.contains(elemento)) throw new RuntimeException("EL CONJUNTO NO CONTIENE EL ELEMENTO DESEADO");
        conjunto.remove(elemento);
        lockDeConjunto.unlock();

        vacios.release();
    }
}
