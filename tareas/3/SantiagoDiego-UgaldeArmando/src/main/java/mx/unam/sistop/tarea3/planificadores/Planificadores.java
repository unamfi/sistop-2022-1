package mx.unam.sistop.tarea3.planificadores;

import mx.unam.sistop.tarea3.CargaAleatoria;
import mx.unam.sistop.tarea3.Resultado;

public class Planificadores {

    public static void ejecutar(CargaAleatoria cargaAleatoria) {
        System.out.println(cargaAleatoria);
        Resultado resultadoFCFS = FirstComeFirstServed.simular(cargaAleatoria);
        System.out.println("\nFCFS:\n" + resultadoFCFS);
    }
}
