import utilidades.Impresor;
import utilidades.UtilidadesNumericas;

import java.util.concurrent.TimeUnit;

public class Calle {
    public static int MAX_CLIENTES_EN_PERIODO = 5;
    public static int TIEMPO_ENTRE_LLEGADAS = 5;
    private final Fila fila;

    private Calle(Fila fila) {
        this.fila = fila;
    }

    private static void imprimirMensaje(String mensaje) {
        Impresor.imprimirAzul("Calle", mensaje);
    }

    public static void iniciar(Fila fila) {
        Calle calle = new Calle(fila);
        imprimirMensaje("Iniciando...");
        new Thread(calle::generarClientesPeriodicamente).start();
    }

    private void generarClientesPeriodicamente() {
        imprimirMensaje("Empezará a generar clientes cada " + TIEMPO_ENTRE_LLEGADAS + " segundos");
        while (true) {
            int clientesPorAgregar = UtilidadesNumericas.obtenerEnteroPositivoAleatorio(MAX_CLIENTES_EN_PERIODO);

            for (int i = 0; i < clientesPorAgregar; i++)
                this.fila.formarCliente(new Cliente());
            imprimirMensaje("Se agregaron " + clientesPorAgregar + " clientes a la fila");

            try {
                TimeUnit.SECONDS.sleep(TIEMPO_ENTRE_LLEGADAS);
            } catch (InterruptedException e) {
                throw new RuntimeException("CALLE FUE INTERRUMPIDA");
            }
        }
    }
}