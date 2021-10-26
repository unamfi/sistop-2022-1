package utilidades;

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ColaSegura<T> {
    private final Semaphore vacios;
    private final Semaphore llenos;
    private final Lock lockDeCola = new ReentrantLock();
    private final Queue<T> cola;

    public ColaSegura(int maximaCapacidad) {
        this.vacios = new Semaphore(maximaCapacidad);
        this.llenos = new Semaphore(0);
        this.cola = new ArrayDeque<>();
    }

    public void encolar(T elemento) {
        try {
            vacios.acquire();
        } catch (InterruptedException e) {
            e.printStackTrace();
            throw new RuntimeException("EL HILO FUE INTERRUMPIDO AL ENCOLAR");
        }

        lockDeCola.lock();
        cola.add(elemento);
        lockDeCola.unlock();

        llenos.release();
    }

    public T desencolar() {
        T desencolado;
        try {
            llenos.acquire();
        } catch (InterruptedException e) {
            e.printStackTrace();
            throw new RuntimeException("EL HILO FUE INTERRUMPIDO AL DESENCOLAR");
        }

        lockDeCola.lock();
        desencolado = cola.remove();
        lockDeCola.unlock();

        vacios.release();
        return desencolado;
    }
}
