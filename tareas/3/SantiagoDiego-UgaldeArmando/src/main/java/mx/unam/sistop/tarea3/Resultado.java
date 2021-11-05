package mx.unam.sistop.tarea3;

import lombok.Value;

@Value
public class Resultado {
    double tiempoDeRespuestaPromedio;
    double tiempoEnEsperaPromedio;
    double proporcionDePenalizacionPromedio;
    String representacion;

    @Override
    public String toString() {
        return "Tiempo de respuesta promedio (T): " + tiempoDeRespuestaPromedio
                + "\nTiempo en espera promedio (E): " + tiempoEnEsperaPromedio
                + "\nProporción de penalización promedio (P): " + proporcionDePenalizacionPromedio
                + "\n" + representacion;
    }
}
