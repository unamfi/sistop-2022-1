import utilidades.Impresor;

import java.util.concurrent.TimeUnit;

public class Pizzero implements Runnable {
    private final Cocina cocina;
    private final int id;
    private final int TIEMPO_DE_PREPARACION = 5;

    public Pizzero(Cocina cocina, int id) {
        this.cocina = cocina;
        this.id = id;
    }

    private static void imprimirMensaje(int id, String mensaje) {
        Impresor.imprimirAzul("Pizzero " + id, mensaje);
    }

    private Pizza prepararPizza() {
        int numeroDePizza = cocina.obtenerNumeroDePizza();
        Pizza pizza = new Pizza(numeroDePizza);

        imprimirMensaje(id, "Haciendo " + pizza);
        try {
            TimeUnit.SECONDS.sleep(TIEMPO_DE_PREPARACION);
        } catch (InterruptedException e) {
            throw new RuntimeException("PIZZERO FUE INTERRUMPIDO");
        }
        imprimirMensaje(id, "La " + pizza + " está lista para hornear");

        return pizza;
    }

    @Override
    public void run() {
        imprimirMensaje(id, "Empezará a hacer pizzas");
        while (true) {
            Pizza pizzaCruda = this.prepararPizza();
            cocina.ponerEnHorno(pizzaCruda);
        }
    }
}

// TODO: Modificar constantes de tiempo públicas
// TODO: Refactorizar nombres de métodos