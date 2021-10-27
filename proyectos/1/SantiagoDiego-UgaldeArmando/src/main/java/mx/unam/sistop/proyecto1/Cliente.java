package mx.unam.sistop.proyecto1;

import mx.unam.sistop.proyecto1.utilidades.AcumuladorSeguro;
import mx.unam.sistop.proyecto1.utilidades.Constantes;
import mx.unam.sistop.proyecto1.utilidades.UtilidadesNumericas;

/**
 * Representa un Cliente a atender. Tendrá un ID único y un número de pizzasDeseadas generado de forma aleatoria con un
 * valor entre 1 y MAX_PIZZAS_POR_CLIENTE.
 */
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
