import utilidades.AcumuladorSeguro;
import utilidades.Constantes;
import utilidades.UtilidadesNumericas;

public class Cliente {
    private static final AcumuladorSeguro clientesGenerados = new AcumuladorSeguro();
    private final int id;
    private int pizzasDeseadas;

    public Cliente() {
        this.id = clientesGenerados.incrementarYObtener();
        this.pizzasDeseadas = UtilidadesNumericas.obtenerEnteroPositivoAleatorio(Constantes.MAX_PIZZAS_POR_CLIENTE);
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
