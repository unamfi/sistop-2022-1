package mx.unam.sistop.tarea3;

import lombok.Value;

@Value
public class Proceso {
    int tiempoDeLlegada;
    int tiempoDeEjecucion;
    String id;

    @Override
    public String toString() {
        return id + ": "
                + "Tiempo de llegada = " + tiempoDeLlegada
                + "\tTiempo de ejecución = " + tiempoDeEjecucion;
    }
}
