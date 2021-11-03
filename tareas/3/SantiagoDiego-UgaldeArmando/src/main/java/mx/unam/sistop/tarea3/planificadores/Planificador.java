package mx.unam.sistop.tarea3.planificadores;

import mx.unam.sistop.tarea3.CargaAleatoria;
import mx.unam.sistop.tarea3.Resultado;

public interface Planificador {
    Resultado simular(CargaAleatoria cargaAleatoria);
}
