public class TrabajadorEnMostrador implements Runnable {

    private final Mostrador mostrador;

    public TrabajadorEnMostrador(Mostrador mostrador) {
        this.mostrador = mostrador;
    }

    @Override
    public void run() {
        while (true) {
            Cliente clientePorAtender = mostrador.llamarCliente();
            for (int i = 0; i < clientePorAtender.obtenerPizzasDeseadas(); i++)
                mostrador.sacarPizzaDelHorno();
        }
    }
}
