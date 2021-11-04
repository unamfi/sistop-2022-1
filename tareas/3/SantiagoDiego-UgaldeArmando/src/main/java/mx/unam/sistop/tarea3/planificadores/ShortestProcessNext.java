package mx.unam.sistop.tarea3.planificadores;

import mx.unam.sistop.tarea3.CargaAleatoria;
import mx.unam.sistop.tarea3.Proceso;
import mx.unam.sistop.tarea3.Resultado;

import java.util.*;

public class ShortestProcessNext {
    public static Resultado simular(CargaAleatoria cargaAleatoria) {
        List<Proceso> procesos = cargaAleatoria.getProcesos();
        Map<Proceso, Integer> tiemposDeFinalizacion = new HashMap<>();
        // Crear min heap para obtener el siguiente proceso más corto a ejecutar en O(log n).
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
            Proceso aEjecutar = minHeap.poll();
            int tiempoDeEjecucion = aEjecutar.getTiempoDeEjecucion();

            for (int i = 0; i < tiempoDeEjecucion; i++) {
                if (tiempo != 0) {
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
