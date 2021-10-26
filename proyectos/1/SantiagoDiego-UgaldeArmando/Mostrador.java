public class Mostrador {
    private static final int TRABAJADORES_EN_MOSTRADOR = 3;
    private final Fila fila;
    private final Horno horno;

    private Mostrador(Fila fila, Horno horno) {
        this.fila = fila;
        this.horno = horno;
    }

    public static void iniciar(Fila fila, Horno horno) {
        Mostrador mostrador = new Mostrador(fila, horno);
        for (int i = 0; i < TRABAJADORES_EN_MOSTRADOR; i++) {
            new Thread(new TrabajadorEnMostrador(mostrador)).start();
        }
    }

    public Cliente llamarCliente() {
        return fila.llamarAlPrimero();
    }

    public Pizza sacarPizzaDelHorno() {
        return horno.sacarPizza();
    }
}
