package mx.unam.sistop.tarea3.planificadores;

import mx.unam.sistop.tarea3.CargaAleatoria;
import mx.unam.sistop.tarea3.Proceso;
import mx.unam.sistop.tarea3.Resultado;

import java.util.*;

public class MultiLevelFeedbackQueue {
    private static final int MAX_COLAS = 10;

    public static Resultado simular(CargaAleatoria cargaAleatoria) {
        // Se inicializan estructuras necesarias.
        Map<Proceso, Integer> tiemposDeFinalizacion = new HashMap<>();
        Map<Proceso, Integer> tiemposDeEjecucionRestantes =
                Planificadores.inicializarTiemposDeEjecucionRestantes(cargaAleatoria);
        List<List<Proceso>> llegadas = Planificadores.obtenerListaDeLlegadas(cargaAleatoria);
        StringBuilder representacion = new StringBuilder();

        // Inicializar colas
        List<Cola> colas = new ArrayList<>();
        for (int i = 0; i < MAX_COLAS; i++) colas.add(new Cola(i + 1));

        Cola primera = colas.get(0);
        int tiempoTotal = cargaAleatoria.getTiempoTotalDeEjecucion();
        int tiempo = 0;

        while (tiempo < tiempoTotal) {
            // Se agregan los procesos que llegan en el tiempo actual.
            List<Proceso> llegan = llegadas.get(tiempo);
            for (Proceso proceso : llegan)
                primera.agregarProceso(proceso);

            // En cada unidad de tiempo se ejecuta un proceso que se encuentre en la primera cola no vacía.
            int primeraNoVaciaIndice = Cola.encontrarPrimeraNoVacia(colas);
            Cola primeraNoVacia = colas.get(primeraNoVaciaIndice);
            Proceso aEjecutar = primeraNoVacia.sacarProceso();
            representacion.append(aEjecutar.getId());

            // Actualizar el tiempo total de ejecución del proceso, además de su tiempo de ejecución en la cola en la
            // que se encuentra,
            tiemposDeEjecucionRestantes.compute(aEjecutar, (k, v) -> v - 1);
            primeraNoVacia.decrementarTiempoDeEjecucionRestante(aEjecutar);

            // El proceso terminó su ejecución, se guarda su tiempo de finalización y se limpia de la cola en la que se
            // encontraba
            if (tiemposDeEjecucionRestantes.get(aEjecutar) == 0) {
                primeraNoVacia.limpiarProceso(aEjecutar);
                tiemposDeFinalizacion.put(aEjecutar, tiempo);
                tiempo++;
                continue;
            }

            // Si ya gastó su quantum y no es la última cola, se pasa a la siguiente.
            if (primeraNoVacia.obtenerTiempoDeEjecucionRestanteEnCola(aEjecutar) == 0 && primeraNoVaciaIndice < MAX_COLAS - 1) {
                primeraNoVacia.limpiarProceso(aEjecutar);
                colas.get(primeraNoVaciaIndice + 1).agregarProceso(aEjecutar);
            }
            // No ha gastado su quantum en esta cola, se regresa a ella.
            else primeraNoVacia.regresarProceso(aEjecutar);

            tiempo++;
        }
        assert Cola.encontrarPrimeraNoVacia(colas) == -1;

        return Planificadores.obtenerResultado(cargaAleatoria, tiemposDeFinalizacion, representacion.toString());
    }

    /**
     * Representa una cola dentro de la cola multinivel.
     */
    public static class Cola {
        /**
         * Tiempo en el que se ejecutará un proceso en esta cola.
         */
        private final int quantum;
        private final Deque<Proceso> procesos = new ArrayDeque<>();
        /**
         * Lleva la cuenta del tiempo restante para cada proceso que se encuentra en la cola.
         */
        private final Map<Proceso, Integer> tiempoDeEjecucionRestanteEnCola = new HashMap<>();

        public Cola(int quantum) {
            this.quantum = quantum;
        }

        /**
         * @param lista Lista de colas donde se buscará.
         * @return El índice de la primera cola no vacía en la lista proporcionada. Si todas están vacías, se retornará
         * -1.
         */
        public static int encontrarPrimeraNoVacia(List<Cola> lista) {
            for (int i = 0; i < lista.size(); i++) {
                Cola cola = lista.get(i);
                if (!cola.estaVacia()) return i;
            }
            return -1;
        }

        public int obtenerTiempoDeEjecucionRestanteEnCola(Proceso proceso) {
            return tiempoDeEjecucionRestanteEnCola.get(proceso);
        }

        public void decrementarTiempoDeEjecucionRestante(Proceso proceso) {
            tiempoDeEjecucionRestanteEnCola.compute(proceso, (k, v) -> v - 1);
        }

        public void agregarProceso(Proceso proceso) {
            tiempoDeEjecucionRestanteEnCola.put(proceso, quantum);
            procesos.addLast(proceso);
        }

        public Proceso sacarProceso() {
            return procesos.pollFirst();
        }

        /**
         * Elimina el mapeo existente del proceso indicado para llevar la cuenta de su tiempo de ejecución en esta
         * cola.
         *
         * @param proceso Proceso del cual se eliminará el mapeo.
         */
        public void limpiarProceso(Proceso proceso) {
            tiempoDeEjecucionRestanteEnCola.remove(proceso);
        }

        /**
         * Regresa el proceso que se sacó a la primera posición de la cola.
         *
         * @param proceso Proceso a regresar a la cola.
         */
        public void regresarProceso(Proceso proceso) {
            procesos.addFirst(proceso);
        }

        public boolean estaVacia() {
            return procesos.isEmpty();
        }
    }
}
