import java.util.concurrent.TimeUnit;

public class Calle implements Runnable {
    public static int MAX_CLIENTES_EN_PERIODO = 5;
    public static int TIEMPO_ENTRE_LLEGADAS = 5;
    private final Fila fila;

    public Calle(Fila fila) {
        this.fila = fila;
    }

    @Override
    public void run() {
        while (true) {
            int clientesPorAgregar = Utilidades.obtenerEnteroPositivoAleatorio(MAX_CLIENTES_EN_PERIODO);

            for (int i = 0; i < clientesPorAgregar; i++)
                this.fila.formarCliente(new Cliente());

            try {
                TimeUnit.SECONDS.sleep(TIEMPO_ENTRE_LLEGADAS);
            } catch (InterruptedException e) {
                throw new RuntimeException("CALLE FUE INTERRUMPIDO");
            }
        }
    }
}

// TODO: Añadir runnable para clases que son hilos.