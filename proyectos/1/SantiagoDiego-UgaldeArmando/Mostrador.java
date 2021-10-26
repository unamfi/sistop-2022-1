import utilidades.Impresor;

public class Mostrador {
    private static final int TRABAJADORES_EN_MOSTRADOR = 3;
    private final Fila fila;
    private final Horno horno;

    private Mostrador(Fila fila, Horno horno) {
        this.fila = fila;
        this.horno = horno;
    }

    private static void imprimirMensaje(String mensaje) {
        Impresor.imprimirRojo("Mostrador", mensaje);
    }

    public static void iniciar(Fila fila, Horno horno) {
        imprimirMensaje("Iniciando...");
        Mostrador mostrador = new Mostrador(fila, horno);
        for (int i = 0; i < TRABAJADORES_EN_MOSTRADOR; i++) {
            int id = i + 1;
            imprimirMensaje("Creando e iniciando TrabajadorEnMostrador " + id + "...");
            new Thread(new TrabajadorEnMostrador(id, mostrador)).start();
        }
        imprimirMensaje("Listo");
    }

    public Cliente llamarCliente() {
        imprimirMensaje("Llamando al siguiente cliente en la fila");
        return fila.llamarAlPrimero();
    }

    public Pizza sacarPizzaListaDelHorno() {
        imprimirMensaje("Sacando pizza del horno...");
        return horno.sacarPizzaLista();
    }
}

// TODO: Añadir documentación y comentarios
