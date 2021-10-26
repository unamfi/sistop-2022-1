import utilidades.UtilidadesNumericas;

import java.util.concurrent.TimeUnit;

public class Calle {
    public static int MAX_CLIENTES_EN_PERIODO = 5;
    public static int TIEMPO_ENTRE_LLEGADAS = 5;
    private final Fila fila;

    private Calle(Fila fila) {
        this.fila = fila;
    }

    public static void iniciar(Fila fila) {
        Calle calle = new Calle(fila);
        System.out.println("Iniciando Calle...");
        new Thread(calle::generarClientesPeriodicamente).start();
    }

    private void generarClientesPeriodicamente() {
        System.out.println("Calle empezará a generar clientes cada " + TIEMPO_ENTRE_LLEGADAS + " segundos");
        while (true) {
            int clientesPorAgregar = UtilidadesNumericas.obtenerEnteroPositivoAleatorio(MAX_CLIENTES_EN_PERIODO);

            for (int i = 0; i < clientesPorAgregar; i++)
                this.fila.formarCliente(new Cliente());
            System.out.println("Se agregaron " + clientesPorAgregar + " clientes");

            try {
                TimeUnit.SECONDS.sleep(TIEMPO_ENTRE_LLEGADAS);
            } catch (InterruptedException e) {
                throw new RuntimeException("CALLE FUE INTERRUMPIDA");
            }
        }
    }
}