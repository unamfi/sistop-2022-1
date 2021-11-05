package mx.unam.sistop.tarea3.planificadores;

import mx.unam.sistop.tarea3.CargaAleatoria;
import mx.unam.sistop.tarea3.Proceso;
import mx.unam.sistop.tarea3.Resultado;
import mx.unam.sistop.tarea3.utilidades.UtilidadesNumericas;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Planificadores {

    public static void ejecutar(CargaAleatoria cargaAleatoria) {
        System.out.println(cargaAleatoria);

        Resultado resultadoFCFS = FirstComeFirstServed.simular(cargaAleatoria);
        System.out.println("\nFCFS:\n" + resultadoFCFS);

        Resultado resultadoRR1 = RoundRobin.simular(cargaAleatoria, 1);
        System.out.println("\nRR1:\n" + resultadoRR1);

        Resultado resultadoRR4 = RoundRobin.simular(cargaAleatoria, 4);
        System.out.println("\nRR4:\n" + resultadoRR4);

        Resultado resultadoSPN = ShortestProcessNext.simular(cargaAleatoria);
        System.out.println("\nSPN:\n" + resultadoSPN);

        Resultado resultadoMLFQ = MultiLevelFeedbackQueue.simular(cargaAleatoria);
        System.out.println("\nMLFQ:\n" + resultadoMLFQ);
    }

    /**
     * Es posible generar las métricas necesarias a partir de los tiempos de finalización e inicio de los procesos. Por
     * lo tanto, cada simulador se encarga únicamente de generar un Map<Proceso, Integer> con los tiempos de
     * finalización, y los tiempos de inicio se encuentran presentes en cada estructura Proceso.
     *
     * @param cargaAleatoria        Carga de procesos planificados.
     * @param tiemposDeFinalizacion Tiempos de finalización de cada proceso.
     * @param representacion        Representación final de la simulación.
     * @return El Resultado con las métricas necesarias.
     */
    public static Resultado obtenerResultado(CargaAleatoria cargaAleatoria, Map<Proceso, Integer> tiemposDeFinalizacion,
                                             String representacion) {
        int numProcesos = cargaAleatoria.getProcesos().size();
        double[] tiemposDeRespuesta = new double[numProcesos];
        double[] tiemposEnEspera = new double[numProcesos];
        double[] proporcionesDePenalizacion = new double[numProcesos];

        // Obtener métricas
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

    /**
     * Obtiene una lista de listas de procesos. La lista ubicada en el índice i contendrá los procesos que llegan en el
     * tiempo i.
     *
     * @param cargaAleatoria Carga de procesos a planificar.
     * @return Lista de listas de procesos que llegan en el tiempo indicado (i, donde i es el índice en el que se
     * encuentra la lista)
     */
    public static List<List<Proceso>> obtenerListaDeLlegadas(CargaAleatoria cargaAleatoria) {
        int tiempoTotal = cargaAleatoria.getTiempoTotalDeEjecucion();
        List<List<Proceso>> llegadas = new ArrayList<>();

        for (int i = 0; i < tiempoTotal; i++) llegadas.add(new ArrayList<>());
        for (Proceso proceso : cargaAleatoria.getProcesos()) llegadas.get(proceso.getTiempoDeLlegada()).add(proceso);

        return llegadas;
    }

    /**
     * Inicializa un mapa con los tiempos de ejecución restantes. Debido a que ningún proceso ha iniciado su ejecución,
     * el tiempo de ejecución restante es el mismo que el tiempo de ejecución original.
     *
     * @param cargaAleatoria Carga de procesos a planificar.
     * @return Mapa con los tiempos de ejecución restantes, que en un inicio son iguales a los tiempos de ejecución
     * originales.
     */
    public static Map<Proceso, Integer> inicializarTiemposDeEjecucionRestantes(CargaAleatoria cargaAleatoria) {
        Map<Proceso, Integer> tiemposDeEjecucionRestantes = new HashMap<>();
        for (Proceso proceso : cargaAleatoria.getProcesos())
            tiemposDeEjecucionRestantes.put(proceso, proceso.getTiempoDeEjecucion());
        return tiemposDeEjecucionRestantes;
    }
}
