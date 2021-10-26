import utilidades.ColaSegura;
import utilidades.ConjuntoSeguro;
import utilidades.Impresor;

import java.util.concurrent.TimeUnit;

public class Horno {
    public static int MAX_PIZZAS_LISTAS = 15;
    public static int MAX_PIZZAS_HORNEANDOSE = 30;
    public static int TIEMPO_DE_HORNEADO = 10;
    private final ColaSegura<Pizza> pizzasListas;
    private final ConjuntoSeguro<Pizza> pizzasHorneandose;

    public Horno() {
        this.pizzasListas = new ColaSegura<>(MAX_PIZZAS_LISTAS);
        this.pizzasHorneandose = new ConjuntoSeguro<>(MAX_PIZZAS_HORNEANDOSE);
    }

    private static void imprimirMensaje(String mensaje) {
        Impresor.imprimirMorado("Horno", mensaje);
    }

    public void hornearPizza(Pizza pizza) {
        pizzasHorneandose.agregar(pizza);
        imprimirMensaje("Horneando " + pizza);
        try {
            TimeUnit.SECONDS.sleep(TIEMPO_DE_HORNEADO);
        } catch (InterruptedException e) {
            throw new RuntimeException("HORNO FUE INTERRUMPIDO");
        }
        pizza.marcarComoHorneada();
        pizzasHorneandose.eliminar(pizza);
        imprimirMensaje("La " + pizza + " está horneada");
        this.pizzasListas.encolar(pizza);
    }

    public Pizza sacarPizzaLista() {
        Pizza pizza = this.pizzasListas.desencolar();
        imprimirMensaje("Se sacó la " + pizza + " del horno");
        return pizza;
    }
}
// TODO: Agregar mensajes de creación de objetos
// TODO: Implementar dejar pizza hornéandose