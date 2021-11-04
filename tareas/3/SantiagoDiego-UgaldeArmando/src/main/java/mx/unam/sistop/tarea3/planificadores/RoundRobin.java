package mx.unam.sistop.tarea3.planificadores;

import mx.unam.sistop.tarea3.CargaAleatoria;
import mx.unam.sistop.tarea3.Proceso;
import mx.unam.sistop.tarea3.Resultado;

import java.util.*;

public class RoundRobin {
    public static Resultado simular(CargaAleatoria cargaAleatoria, int duracionDeRound) {
        Map<Proceso, Integer> tiemposDeFinalizacion = new HashMap<>();
        Map<Proceso, Integer> tiemposDeEjecucionRestantes = Planificadores.inicializarTiemposDeEjecucionRestantes(cargaAleatoria);
        List<List<Proceso>> llegadas = Planificadores.obtenerListaDeLlegadas(cargaAleatoria);
        StringBuilder representacion = new StringBuilder();

        // Inicializar cola doble con procesos que llegan en el tiempo 0
        Deque<Proceso> ejecutandose = new ArrayDeque<>(llegadas.get(0));

        int tiempoTotal = cargaAleatoria.getTiempoTotalDeEjecucion();
        int tiempo = 0;
        while (tiempo < tiempoTotal) {
            assert !ejecutandose.isEmpty();
            Proceso aEjecutar = ejecutandose.pollFirst();
            int periodo = Math.min(duracionDeRound, tiemposDeEjecucionRestantes.get(aEjecutar));

            for (int i = 0; i < periodo; i++) {
                if (tiempo != 0) {
                    List<Proceso> llegan = llegadas.get(tiempo);
                    for (Proceso proceso : llegan) ejecutandose.addFirst(proceso);
                }

                representacion.append(aEjecutar.getId());
                tiempo++;
            }
            tiemposDeEjecucionRestantes.compute(aEjecutar, (k, v) -> v - periodo);
            if (tiemposDeEjecucionRestantes.get(aEjecutar) == 0) tiemposDeFinalizacion.put(aEjecutar, tiempo - 1);
            else ejecutandose.addLast(aEjecutar);
        }
        assert ejecutandose.isEmpty();

        return Planificadores.obtenerResultado(cargaAleatoria, tiemposDeFinalizacion, representacion.toString());
    }
}
