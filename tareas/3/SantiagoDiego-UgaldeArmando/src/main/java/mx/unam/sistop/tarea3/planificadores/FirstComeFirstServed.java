package mx.unam.sistop.tarea3.planificadores;

import mx.unam.sistop.tarea3.CargaAleatoria;
import mx.unam.sistop.tarea3.Proceso;
import mx.unam.sistop.tarea3.Resultado;

import java.util.HashMap;
import java.util.Map;

public class FirstComeFirstServed {
    public static Resultado simular(CargaAleatoria cargaAleatoria) {
        Map<Proceso, Integer> tiemposDeFinalizacion = new HashMap<>();

        StringBuilder representacion = new StringBuilder();

        int tiempo = 0;
        // Se toma en cuenta que la lista de procesos se encuentra ordenada acorde a los tiempos de llegada.
        for (Proceso proceso : cargaAleatoria.getProcesos()) {
            String id = proceso.getId();
            for (int i = 0; i < proceso.getTiempoDeEjecucion(); i++) {
                representacion.append(id);
                tiempo++;
            }
            tiemposDeFinalizacion.put(proceso, tiempo - 1);
        }

        return Planificadores.obtenerResultado(cargaAleatoria, tiemposDeFinalizacion, representacion.toString());
    }
}
