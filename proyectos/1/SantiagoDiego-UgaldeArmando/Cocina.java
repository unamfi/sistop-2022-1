import utilidades.AcumuladorSeguro;
import utilidades.Impresor;

import java.util.concurrent.TimeUnit;

public class Cocina {
    //public static int MAX_PIZZAS_EN_INVENTARIO = 1000;
    public static int PIZZEROS = 3;
    public static int TIEMPO_PARA_PONER_PIZZA_EN_HORNO = 2;
    //private boolean trabajando = true;
    private final AcumuladorSeguro pizzasProducidas = new AcumuladorSeguro();
    private final Horno horno;

    private Cocina(Horno horno) {
        this.horno = horno;
    }

    private static void imprimirMensaje(String mensaje) {
        Impresor.imprimirAmarillo("Cocina", mensaje);
    }

    public static void iniciar(Horno horno) {
        Cocina cocina = new Cocina(horno);
        imprimirMensaje("Iniciando...");
        for (int i = 0; i < PIZZEROS; i++) {
            int id = i + 1;
            imprimirMensaje("Creando e iniciando Pizzero " + id + "...");
            new Thread(new Pizzero(cocina, id)).start();
        }
        imprimirMensaje("Lista");
    }

    public int obtenerNumeroDePizza() {
        return pizzasProducidas.incrementarYObtener();
    }

    public void ponerEnHorno(Pizza pizzaCruda) {
        imprimirMensaje("Poniendo " + pizzaCruda + " en el horno");
        try {
            TimeUnit.SECONDS.sleep(TIEMPO_PARA_PONER_PIZZA_EN_HORNO);
        } catch (InterruptedException e) {
            throw new RuntimeException("COCINA FUE INTERRUMPIDA");
        }
        horno.hornearPizza(pizzaCruda);
    }
}
// TODO: Implementar checar inventario.
