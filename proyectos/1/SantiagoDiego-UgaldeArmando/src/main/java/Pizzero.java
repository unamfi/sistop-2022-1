import utilidades.Constantes;
import utilidades.Impresor;
import utilidades.Logger;

import java.util.concurrent.TimeUnit;

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