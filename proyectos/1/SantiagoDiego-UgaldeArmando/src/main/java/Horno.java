import utilidades.*;

import java.util.concurrent.TimeUnit;

/**
 * Representa el Horno del establecimiento y funcionará como un buffer con dos divisiones: las pizzasListas y las
 * pizzasHorneandose. Cada una de estas partes tendrá cierta capacidad, especificadas por MAX_PIZZAS_LISTAS y
 * MAX_PIZZAS_HORNEANDOSE, respectivamente. Cuando un Pizzero desea hornear una pizza, primero se coloca en
 * pizzasHorneandose, y, una vez que está lista, se pasa a pizzasListas (en este punto podríamos decir que el Pizzero
 * produjo la pizza), donde los TrabajadoresDeMostrador podrán retirarlas (consumirlas).
 */
public class Horno implements Logger {
    private final ColaSegura<Pizza> pizzasListas;
    private final ConjuntoSeguro<Pizza> pizzasHorneandose;

    public Horno() {
        this.pizzasListas = new ColaSegura<>(Constantes.MAX_PIZZAS_LISTAS);
        this.pizzasHorneandose = new ConjuntoSeguro<>(Constantes.MAX_PIZZAS_HORNEANDOSE);
    }

    public void imprimirMensaje(String mensaje) {
        Impresor.imprimirMorado("Horno", mensaje);
    }

    public void hornearPizza(Pizza pizza) {
        pizzasHorneandose.agregar(pizza);
        imprimirMensaje("Horneando " + pizza);
        try {
            TimeUnit.SECONDS.sleep(Constantes.TIEMPO_DE_HORNEADO);
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