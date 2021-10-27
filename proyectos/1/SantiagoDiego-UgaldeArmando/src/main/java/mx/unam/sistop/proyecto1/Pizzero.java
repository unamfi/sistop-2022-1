package mx.unam.sistop.proyecto1;

import mx.unam.sistop.proyecto1.utilidades.Constantes;
import mx.unam.sistop.proyecto1.utilidades.Impresor;
import mx.unam.sistop.proyecto1.utilidades.Logger;

import java.util.concurrent.TimeUnit;

/**
 * Representa a un trabajador de la Cocina. Se puede considerar que es un productor, ya que está encargado de preparar
 * las pizzas, meterlas al horno, esperar a que se horneen, y finalmente pasarlas al horno de pizzas listas (buffer).
 * Los detalles de esta funcionalidad se encuentran implementados en el método ponerEnHorno de la clase Cocina. Además,
 * es importante mencionar que un Pizzero siempre tratará de que el horno esté lleno, es decir, no parará a menos de que
 * el Horno esté lleno.
 */
public class Pizzero implements Runnable, Logger {
    private final Cocina cocina;
    private final int id;

    public Pizzero(Cocina cocina, int id) {
        this.cocina = cocina;
        this.id = id;
    }

    public void imprimirMensaje(String mensaje) {
        Impresor.imprimirAzul("Pizzero " + this.id, mensaje);
    }

    private Pizza prepararPizza() {
        int numeroDePizza = cocina.obtenerNumeroDePizza();
        Pizza pizza = new Pizza(numeroDePizza);

        this.imprimirMensaje("Haciendo " + pizza);
        try {
            TimeUnit.SECONDS.sleep(Constantes.TIEMPO_DE_PREPARACION_DE_PIZZA);
        } catch (InterruptedException e) {
            throw new RuntimeException("PIZZERO FUE INTERRUMPIDO");
        }
        this.imprimirMensaje("La " + pizza + " está lista para hornear");

        return pizza;
    }

    @Override
    public void run() {
        this.imprimirMensaje("Empezará a hacer pizzas");
        while (true) {
            Pizza pizzaCruda = this.prepararPizza();
            cocina.ponerEnHorno(pizzaCruda);
        }
    }
}

// TODO: Refactorizar nombres de métodos