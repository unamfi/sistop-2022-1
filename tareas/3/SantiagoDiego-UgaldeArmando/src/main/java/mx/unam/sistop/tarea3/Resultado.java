package mx.unam.sistop.tarea3;

import lombok.Value;

@Value
public class Resultado {
    int tiempoDeRespuesta;
    int tiempoEnEspera;
    int proporcionDePenalizacion;
    String representacion;
}
