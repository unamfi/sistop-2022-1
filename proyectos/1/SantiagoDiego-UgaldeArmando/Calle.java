import utilidades.Impresor;
import utilidades.Logger;
import utilidades.UtilidadesNumericas;

import java.util.concurrent.TimeUnit;

public class Calle implements Logger {
    private static final int MAX_CLIENTES_EN_PERIODO = 5;
    private static final int TIEMPO_ENTRE_LLEGADAS = 15;
    private final Fila fila;

    private Calle(Fila fila) {
        this.fila = fila;
    }

    public static void iniciar(Fila fila) {
        Calle calle = new Calle(fila);
        calle.imprimirMensaje("Iniciando...");
        new Thread(calle::generarClientesPeriodicamente).start();
        calle.imprimirMensaje("Lista");
    }

    public void imprimirMensaje(String mensaje) {
        Impresor.imprimirBlanco("Calle", mensaje);
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