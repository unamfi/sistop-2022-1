package mx.unam.sistop.tarea3.planificadores;

import mx.unam.sistop.tarea3.CargaAleatoria;
import mx.unam.sistop.tarea3.Proceso;
import mx.unam.sistop.tarea3.Resultado;

import java.util.*;

public class RoundRobin {
    public static Resultado simular(CargaAleatoria cargaAleatoria, int duracionDeRound) {
        List<Proceso> procesos = cargaAleatoria.getProcesos();
        Map<Proceso, Integer> tiemposDeFinalizacion = new HashMap<>();
        Map<Proceso, Integer> tiemposDeEjecucionRestantes = new HashMap<>();
        for (Proceso proceso : procesos) tiemposDeEjecucionRestantes.put(proceso, proceso.getTiempoDeEjecucion());

        // Crear lista con listas de todos los procesos que llegan en determinado tiempo.
        int tiempoTotal = cargaAleatoria.getTiempoTotalDeEjecucion();
        List<List<Proceso>> llegadas = new ArrayList<>();
        for (int i = 0; i < tiempoTotal; i++) llegadas.add(new ArrayList<>());
        for (Proceso proceso : procesos) llegadas.get(proceso.getTiempoDeLlegada()).add(proceso);

        StringBuilder representacion = new StringBuilder();
        Deque<Proceso> ejecutandose = new ArrayDeque<>();

        // Inicializar cola doble con procesos que llegan en el tiempo 0
        for (Proceso proceso : llegadas.get(0)) ejecutandose.addLast(proceso);

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
            if (tiemposDeEjecucionRestantes.get(aEjecutar) == 0) tiemposDeFinalizacion.put(aEjecutar, tiempo);
            else ejecutandose.addLast(aEjecutar);
        }
        assert ejecutandose.isEmpty();

        return Planificadores.obtenerResultado(cargaAleatoria, tiemposDeFinalizacion, representacion.toString());
    }
}
