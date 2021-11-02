package mx.unam.sistop.tarea3;

import lombok.Value;

@Value
public class Resultado {
    int tiempoDeRespuesta;
    int tiempoEnEspera;
    int proporcionDePenalizacion;
    String representacion;

    @Override
    public String toString() {
        return "Tiempo de respuesta (T): " + tiempoDeRespuesta
                + "\nTiempo en espera (E): " + tiempoEnEspera
                + "\nProporción de penalización (P): " + proporcionDePenalizacion
                + "\n" + representacion;
    }
}
