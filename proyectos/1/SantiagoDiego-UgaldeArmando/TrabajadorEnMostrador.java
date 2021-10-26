import utilidades.Impresor;

public class TrabajadorEnMostrador implements Runnable {

    private final Mostrador mostrador;
    private final int id;

    public TrabajadorEnMostrador(int id, Mostrador mostrador) {
        this.mostrador = mostrador;
        this.id = id;
    }

    private static void imprimirMensaje(int id, String mensaje) {
        Impresor.imprimirBlanco("Trabajador en mostrador " + id, mensaje);
    }

    @Override
    public void run() {
        while (true) {
            Cliente clientePorAtender = mostrador.llamarCliente();
            imprimirMensaje(id, "Atendiendo " + clientePorAtender);
            for (int i = 0; i < clientePorAtender.obtenerPizzasDeseadas(); i++) {
                Pizza pizza = mostrador.sacarPizzaListaDelHorno();
                imprimirMensaje(id, "Dándole la " + pizza + " al " + clientePorAtender);
            }
            imprimirMensaje(id, "El " + clientePorAtender + " ha sido atendido");
        }
    }
}

// TODO: Añadir argumentos de línea de comandos