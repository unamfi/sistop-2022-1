import utilidades.AcumuladorSeguro;
import utilidades.UtilidadesNumericas;

public class Cliente {
    private static final AcumuladorSeguro clientesGenerados = new AcumuladorSeguro();
    private static final int MAX_PIZZAS = 5;
    private final int id;
    private int pizzasDeseadas;

    public Cliente() {
        this.id = clientesGenerados.incrementarYObtener();
        this.pizzasDeseadas = UtilidadesNumericas.obtenerEnteroPositivoAleatorio(MAX_PIZZAS);
    }

    public int obtenerPizzasDeseadas() {
        return pizzasDeseadas;
    }

    public void actualizarPizzasDeseadas(int nuevoValor) {
        this.pizzasDeseadas = nuevoValor;
    }

    @Override
    public String toString() {
        return "cliente " + id;
    }
}
