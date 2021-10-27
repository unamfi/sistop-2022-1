package mx.unam.sistop.proyecto1;

import mx.unam.sistop.proyecto1.utilidades.Impresor;
import mx.unam.sistop.proyecto1.utilidades.Logger;

/**
 * Representa un trabajador del mostrador. Atenderán a los Clientes llamando al primero de la Fila (para consumirlo)
 * cuando no se esté atendiendo a otro, y se tomarán las pizzas (se consumirán) que el cliente desee del Horno hasta que
 * se le proporcionen las que desee. En este punto, el cliente ha sido atendido y se procede a atender al siguiente, si
 * es que lo hay. Podemos decir que son "dobles consumidores", es decir, consumen Clientes de la fila y consumen Pizzas
 * del Horno.
 */
public class TrabajadorEnMostrador implements Runnable, Logger {
    private final Mostrador mostrador;
    private final int id;

    public TrabajadorEnMostrador(int id, Mostrador mostrador) {
        this.mostrador = mostrador;
        this.id = id;
    }

    public void imprimirMensaje(String mensaje) {
        Impresor.imprimirAzul("Trabajador en mostrador " + this.id, mensaje);
    }

    @Override
    public void run() {
        while (true) {
            Cliente clientePorAtender = mostrador.llamarCliente();
            this.imprimirMensaje("Atendiendo " + clientePorAtender
                    + " (" + clientePorAtender.obtenerPizzasDeseadas() + " pizzas)");
            for (int i = 0; i < clientePorAtender.obtenerPizzasDeseadas(); i++) {
                Pizza pizza = mostrador.sacarPizzaListaDelHorno();
                imprimirMensaje("Dándole la " + pizza + " al " + clientePorAtender);
            }
            imprimirMensaje("El " + clientePorAtender + " ha sido atendido");
        }
    }
}