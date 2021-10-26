import java.util.concurrent.TimeUnit;

public class Pizzero implements Runnable {
    private final Cocina cocina;
    private final int TIEMPO_DE_PREPARACION = 5;

    public Pizzero(Cocina cocina) {
        this.cocina = cocina;
    }

    private Pizza hacerPizza() {
        int numeroDePizza = cocina.obtenerNumeroDePizza();

        try {
            TimeUnit.SECONDS.sleep(TIEMPO_DE_PREPARACION);
        } catch (InterruptedException e) {
            throw new RuntimeException("PIZZERO FUE INTERRUMPIDO");
        }

        return new Pizza(numeroDePizza);
    }

    @Override
    public void run() {
        while (true) {
            Pizza pizzaCruda = this.hacerPizza();
            cocina.ponerEnHorno(pizzaCruda);
        }
    }
}

// TODO: Modificar constantes de tiempo públicas