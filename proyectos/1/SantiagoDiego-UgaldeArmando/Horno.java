import utilidades.ColaSegura;
import utilidades.Impresor;

import java.util.concurrent.TimeUnit;

public class Horno {
    public static int MAX_PIZZAS = 15;
    public static int TIEMPO_DE_HORNEADO = 10;
    private final ColaSegura<Pizza> pizzasListas;

    public Horno() {
        this.pizzasListas = new ColaSegura<>(MAX_PIZZAS);
    }

    private static void imprimirMensaje(String mensaje) {
        Impresor.imprimirMorado("Horno", mensaje);
    }

    public void hornearPizza(Pizza pizza) {
        imprimirMensaje("Horneando " + pizza);
        try {
            TimeUnit.SECONDS.sleep(TIEMPO_DE_HORNEADO);
        } catch (InterruptedException e) {
            throw new RuntimeException("HORNO FUE INTERRUMPIDO");
        }
        pizza.marcarComoHorneada();
        imprimirMensaje("La " + pizza + " está horneada");
        this.pizzasListas.encolar(pizza);
    }

    public Pizza sacarPizza() {
        Pizza pizza = this.pizzasListas.desencolar();
        imprimirMensaje("Se sacó la " + pizza + " del horno");
        return pizza;
    }
}
// TODO: Agregar mensajes de creación de objetos