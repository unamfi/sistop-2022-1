package mx.unam.sistop.tarea3.planificadores;

import mx.unam.sistop.tarea3.CargaAleatoria;
import mx.unam.sistop.tarea3.Proceso;
import mx.unam.sistop.tarea3.Resultado;
import mx.unam.sistop.tarea3.utilidades.UtilidadesNumericas;

import java.util.HashMap;
import java.util.Map;

public class FirstComeFirstServed {
    public static Resultado simular(CargaAleatoria cargaAleatoria) {
        Map<Proceso, Integer> tiemposDeFinalizacion = new HashMap<>();
        int numProcesos = cargaAleatoria.getProcesos().size();
        double[] tiemposDeRespuesta = new double[numProcesos];
        double[] tiemposEnEspera = new double[numProcesos];
        double[] proporcionesDePenalizacion = new double[numProcesos];
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

        // Obtener tiempos
        int j = 0;
        for (Proceso proceso : cargaAleatoria.getProcesos()) {
            tiemposDeRespuesta[j] = tiemposDeFinalizacion.get(proceso) - proceso.getTiempoDeLlegada() + 1;
            tiemposEnEspera[j] = tiemposDeRespuesta[j] - proceso.getTiempoDeEjecucion();
            proporcionesDePenalizacion[j] = tiemposDeRespuesta[j] / proceso.getTiempoDeEjecucion();
            j++;
        }

        double tiempoDeRespuestaPromedio = UtilidadesNumericas.obtenerPromedio(tiemposDeRespuesta);
        double tiempoEnEsperaPromedio = UtilidadesNumericas.obtenerPromedio(tiemposEnEspera);
        double proporcionDePenalizacionPromedio = UtilidadesNumericas.obtenerPromedio(proporcionesDePenalizacion);
        return new Resultado(tiempoDeRespuestaPromedio,
                tiempoEnEsperaPromedio,
                proporcionDePenalizacionPromedio,
                representacion.toString());
    }
}
