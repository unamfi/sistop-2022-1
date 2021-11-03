package mx.unam.sistop.tarea3.planificadores;

import mx.unam.sistop.tarea3.CargaAleatoria;
import mx.unam.sistop.tarea3.Proceso;
import mx.unam.sistop.tarea3.Resultado;
import mx.unam.sistop.tarea3.utilidades.UtilidadesNumericas;

import java.util.Map;

public class Planificadores {

    public static void ejecutar(CargaAleatoria cargaAleatoria) {
        System.out.println(cargaAleatoria);
        Resultado resultadoFCFS = FirstComeFirstServed.simular(cargaAleatoria);
        System.out.println("\nFCFS:\n" + resultadoFCFS);
    }

    public static Resultado obtenerResultado(CargaAleatoria cargaAleatoria, Map<Proceso, Integer> tiemposDeFinalizacion,
                                             String representacion) {
        int numProcesos = cargaAleatoria.getProcesos().size();
        double[] tiemposDeRespuesta = new double[numProcesos];
        double[] tiemposEnEspera = new double[numProcesos];
        double[] proporcionesDePenalizacion = new double[numProcesos];

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
                representacion);
    }
}
