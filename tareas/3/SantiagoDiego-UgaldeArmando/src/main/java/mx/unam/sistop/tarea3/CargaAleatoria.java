package mx.unam.sistop.tarea3;

import lombok.Value;

import java.util.List;

@Value
public class CargaAleatoria {
    List<Proceso> procesos;

    public int getTiempoTotalDeEjecucion() {
        return procesos.stream()
                .mapToInt(Proceso::getTiempoDeEjecucion)
                .reduce(0, Integer::sum);
    }
}
