import java.util.concurrent.TimeUnit;

public class Horno {
    public static int MAX_PIZZAS = 15;
    public static int TIEMPO_DE_HORNEADO = 10;
    private final ColaSegura<Pizza> pizzasListas;

    public Horno() {
        this.pizzasListas = new ColaSegura<>(MAX_PIZZAS);
    }

    public void hornearPizza(Pizza pizza) {
        try {
            TimeUnit.SECONDS.sleep(TIEMPO_DE_HORNEADO);
        } catch (InterruptedException e) {
            throw new RuntimeException("HORNO FUE INTERRUMPIDO");
        }
        pizza.marcarComoHorneada();
        this.pizzasListas.encolar(pizza);
    }

    public Pizza sacarPizza() {
        return this.pizzasListas.desencolar();
    }
}