import utilidades.Constantes;
import utilidades.Impresor;
import utilidades.Logger;
import utilidades.UtilidadesNumericas;

import java.util.concurrent.TimeUnit;

public class Calle implements Logger {
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
        imprimirMensaje("Empezará a generar clientes cada " + Constantes.TIEMPO_ENTRE_LLEGADA_DE_CLIENTES + " segundos");
        while (true) {
            int clientesPorAgregar = UtilidadesNumericas.obtenerEnteroPositivoAleatorio(Constantes.MAX_CLIENTES_EN_PERIODO);

            for (int i = 0; i < clientesPorAgregar; i++)
                this.fila.formarCliente(new Cliente());
            imprimirMensaje("Se agregaron " + clientesPorAgregar + " clientes a la fila");

            try {
                TimeUnit.SECONDS.sleep(Constantes.TIEMPO_ENTRE_LLEGADA_DE_CLIENTES);
            } catch (InterruptedException e) {
                throw new RuntimeException("CALLE FUE INTERRUMPIDA");
            }
        }
    }
}