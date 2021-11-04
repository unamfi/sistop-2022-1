package mx.unam.sistop.tarea3.planificadores;

import mx.unam.sistop.tarea3.CargaAleatoria;
import mx.unam.sistop.tarea3.Proceso;
import mx.unam.sistop.tarea3.Resultado;

import java.util.*;

public class RoundRobin {
    public static Resultado simular(CargaAleatoria cargaAleatoria, int duracionDeRound) {
        // Se inicializan estructuras necesarias.
        Map<Proceso, Integer> tiemposDeFinalizacion = new HashMap<>();
        Map<Proceso, Integer> tiemposDeEjecucionRestantes =
                Planificadores.inicializarTiemposDeEjecucionRestantes(cargaAleatoria);
        List<List<Proceso>> llegadas = Planificadores.obtenerListaDeLlegadas(cargaAleatoria);
        StringBuilder representacion = new StringBuilder();

        // Inicializar cola doble con procesos que llegan en el tiempo 0
        Deque<Proceso> ejecutandose = new ArrayDeque<>(llegadas.get(0));

        int tiempoTotal = cargaAleatoria.getTiempoTotalDeEjecucion();
        int tiempo = 0;
        while (tiempo < tiempoTotal) {
            assert !ejecutandose.isEmpty();
            // Ejecutar el primer proceso en la cola de procesos ejecutándose.
            Proceso aEjecutar = ejecutandose.pollFirst();
            // El tiempo de ejecución será el round establecido. Si el tiempo de ejecución restante del proceso a
            // ejecutar es menor que el round, se ejecutará únicamente por el tiempo restante.
            int periodo = Math.min(duracionDeRound, tiemposDeEjecucionRestantes.get(aEjecutar));

            // Ejecutar el proceso por el periodo establecido.
            for (int i = 0; i < periodo; i++) {
                // Debido a que la cola se inicializó con los procesos que llegan en el tiempo 0, no se deben de
                // agregar nuevamente.
                if (tiempo != 0) {
                    // Se agregan los procesos que llegan en el tiempo actual a la cola de procesos ejecutándose.
                    List<Proceso> llegan = llegadas.get(tiempo);
                    // Se ponen "al principio de la fila" para optimizar su tiempo de respuesta.
                    for (Proceso proceso : llegan) ejecutandose.addFirst(proceso);
                }

                representacion.append(aEjecutar.getId());
                tiempo++;
            }

            // Se actualiza su tiempo de ejecución.
            tiemposDeEjecucionRestantes.compute(aEjecutar, (k, v) -> v - periodo);
            // Si ya terminó de ejecutarse, se guarda su tiempo de finalización y no se vuelve a encolar.
            if (tiemposDeEjecucionRestantes.get(aEjecutar) == 0) tiemposDeFinalizacion.put(aEjecutar, tiempo - 1);
                // Si aún no termina, se encola nuevamente pero "al final de la fila".
            else ejecutandose.addLast(aEjecutar);
        }
        assert ejecutandose.isEmpty();

        return Planificadores.obtenerResultado(cargaAleatoria, tiemposDeFinalizacion, representacion.toString());
    }
}
