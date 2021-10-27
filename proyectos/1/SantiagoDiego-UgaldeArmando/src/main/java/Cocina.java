import utilidades.AcumuladorSeguro;
import utilidades.Constantes;
import utilidades.Impresor;
import utilidades.Logger;

import java.util.concurrent.TimeUnit;

public class Cocina implements Logger {
    //private boolean trabajando = true;
    private final AcumuladorSeguro pizzasProducidas = new AcumuladorSeguro();
    private final Horno horno;

    private Cocina(Horno horno) {
        this.horno = horno;
    }

    public static void iniciar(Horno horno) {
        Cocina cocina = new Cocina(horno);
        cocina.imprimirMensaje("Iniciando...");
        for (int i = 0; i < Constantes.PIZZEROS; i++) {
            int id = i + 1;
            cocina.imprimirMensaje("Creando e iniciando Pizzero " + id + "...");
            new Thread(new Pizzero(cocina, id)).start();
        }
        cocina.imprimirMensaje("Lista");
    }

    public void imprimirMensaje(String mensaje) {
        Impresor.imprimirAmarillo("Cocina", mensaje);
    }

    public int obtenerNumeroDePizza() {
        return pizzasProducidas.incrementarYObtener();
    }

    public void ponerEnHorno(Pizza pizzaCruda) {
        imprimirMensaje("Poniendo " + pizzaCruda + " en el horno");
        try {
            TimeUnit.SECONDS.sleep(Constantes.TIEMPO_PARA_PONER_PIZZA_EN_HORNO);
        } catch (InterruptedException e) {
            throw new RuntimeException("COCINA FUE INTERRUMPIDA");
        }
        horno.hornearPizza(pizzaCruda);
    }
}
// TODO: Implementar checar inventario.
