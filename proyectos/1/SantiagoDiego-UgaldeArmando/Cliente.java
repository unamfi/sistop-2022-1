import utilidades.UtilidadesNumericas;

public class Cliente {
    public static int MAX_PIZZAS = 10;
    private int pizzasDeseadas;

    public Cliente() {
        this.pizzasDeseadas = UtilidadesNumericas.obtenerEnteroPositivoAleatorio(MAX_PIZZAS);
    }

    public int obtenerPizzasDeseadas() {
        return pizzasDeseadas;
    }

    public void actualizarPizzasDeseadas(int nuevoValor) {
        this.pizzasDeseadas = nuevoValor;
    }
}
