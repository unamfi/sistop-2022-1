package mx.unam.sistop.tarea3;

import lombok.Value;

@Value
public class Proceso {
    int tiempoDeLlegada;
    int tiempoDeEjecucion;

    @Override
    public String toString() {
        return "Tiempo de llegada = " + tiempoDeLlegada + "\tTiempo de ejecución = " + tiempoDeEjecucion;
    }
}
