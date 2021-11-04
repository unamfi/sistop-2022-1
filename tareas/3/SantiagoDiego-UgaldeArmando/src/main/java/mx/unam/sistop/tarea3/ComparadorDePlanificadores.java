package mx.unam.sistop.tarea3;

import mx.unam.sistop.tarea3.planificadores.Planificadores;

public class ComparadorDePlanificadores {
    private static final int RONDAS = 5;

    public static void main(String[] args) {
        // Realizar las rondas de simulación indicadas, cada una con una carga aleatoria.
        for (int i = 0; i < RONDAS; i++) {
            System.out.println("Ronda " + (i + 1) + ":");
            Planificadores.ejecutar(CargaAleatoria.generar());
            System.out.println();
        }
    }
}
