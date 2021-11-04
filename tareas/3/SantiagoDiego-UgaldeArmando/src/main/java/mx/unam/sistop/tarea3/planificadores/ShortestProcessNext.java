package mx.unam.sistop.tarea3.planificadores;

import mx.unam.sistop.tarea3.CargaAleatoria;
import mx.unam.sistop.tarea3.Proceso;
import mx.unam.sistop.tarea3.Resultado;

import java.util.*;

public class ShortestProcessNext {
    public static Resultado simular(CargaAleatoria cargaAleatoria) {
        Map<Proceso, Integer> tiemposDeFinalizacion = new HashMap<>();
        // Crear min heap para obtener el siguiente proceso más corto a ejecutar en O(log n), donde n es el número de
        // procesos que se encuentran en el heap. En el peor de los casos, n puede ser igual al total de procesos.
        PriorityQueue<Proceso> minHeap = new PriorityQueue<>(Comparator.comparingInt(Proceso::getTiempoDeEjecucion));

        // Crear lista con listas de todos los procesos que llegan en determinado tiempo.
        List<List<Proceso>> llegadas = Planificadores.obtenerListaDeLlegadas(cargaAleatoria);

        StringBuilder representacion = new StringBuilder();

        // Inicializar heap con procesos que llegan en el tiempo 0
        minHeap.addAll(llegadas.get(0));

        int tiempoTotal = cargaAleatoria.getTiempoTotalDeEjecucion();
        int tiempo = 0;
        while (tiempo < tiempoTotal) {
            assert !minHeap.isEmpty();
            // Se escoge el proceso con menor tiempo de ejecución.
            Proceso aEjecutar = minHeap.poll();
            int tiempoDeEjecucion = aEjecutar.getTiempoDeEjecucion();

            // Se ejecuta por el total de su tiempo.
            for (int i = 0; i < tiempoDeEjecucion; i++) {
                // Debido a que el heap se inicializó con los procesos que llegan en el tiempo 0, no se deben de
                // agregar nuevamente.
                if (tiempo != 0) {
                    // Se agregan todos los procesos que llegan en el tiempo actual.
                    List<Proceso> llegan = llegadas.get(tiempo);
                    minHeap.addAll(llegan);
                }

                representacion.append(aEjecutar.getId());
                tiempo++;
            }

            tiemposDeFinalizacion.put(aEjecutar, tiempo - 1);
        }
        assert minHeap.isEmpty();

        return Planificadores.obtenerResultado(cargaAleatoria, tiemposDeFinalizacion, representacion.toString());
    }
}
