import utilidades.Impresor;
import utilidades.Logger;

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