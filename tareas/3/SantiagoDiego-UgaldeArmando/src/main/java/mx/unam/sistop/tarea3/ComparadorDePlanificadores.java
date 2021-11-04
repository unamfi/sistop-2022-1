package mx.unam.sistop.tarea3;

import mx.unam.sistop.tarea3.planificadores.Planificadores;

import java.util.ArrayList;
import java.util.List;

public class ComparadorDePlanificadores {
    private static final int RONDAS = 5;

    public static void main(String[] args) {
        // Prueba para carga utilizada en diapositivas.
        List<Proceso> procesos = new ArrayList<>();
        procesos.add(new Proceso(0, 3, "A"));
        procesos.add(new Proceso(1, 5, "B"));
        procesos.add(new Proceso(3, 2, "C"));
        procesos.add(new Proceso(9, 5, "D"));
        procesos.add(new Proceso(12, 5, "E"));
        System.out.println("Prueba utilizando la carga presentada en la diapositiva:");
        Planificadores.ejecutar(new CargaAleatoria(procesos));
        System.out.println();

        // Realizar las rondas de simulación indicadas, cada una con una carga aleatoria.
        for (int i = 0; i < RONDAS; i++) {
            System.out.println("Ronda " + (i + 1) + ":");
            Planificadores.ejecutar(CargaAleatoria.generar());
            System.out.println();
        }
    }
}
