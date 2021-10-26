public class TrabajadorEnMostrador implements Runnable {

    private final Mostrador mostrador;
    private final int id;

    public TrabajadorEnMostrador(int id, Mostrador mostrador) {
        this.mostrador = mostrador;
        this.id = id;
    }

    @Override
    public void run() {
        while (true) {
            Cliente clientePorAtender = mostrador.llamarCliente();
            for (int i = 0; i < clientePorAtender.obtenerPizzasDeseadas(); i++)
                mostrador.sacarPizzaListaDelHorno();
        }
    }
}
