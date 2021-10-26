import utilidades.AcumuladorSeguro;

public class Cocina {
    //public static int MAX_PIZZAS_EN_INVENTARIO = 1000;
    public static int PIZZEROS = 3;
    //private boolean trabajando = true;
    private final AcumuladorSeguro pizzasProducidas = new AcumuladorSeguro();
    private final Horno horno;

    private Cocina(Horno horno) {
        this.horno = horno;
    }

    public static void iniciar(Horno horno) {
        Cocina cocina = new Cocina(horno);
        for (int i = 0; i < PIZZEROS; i++) {
            new Thread(new Pizzero(cocina)).start();
        }
    }

    public int obtenerNumeroDePizza() {
        return pizzasProducidas.incrementarYObtener();
    }

    public void ponerEnHorno(Pizza pizzaCruda) {
        horno.hornearPizza(pizzaCruda);
    }
}
// TODO: Implementar checar inventario.
