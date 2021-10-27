package mx.unam.sistop.proyecto1;

import mx.unam.sistop.proyecto1.utilidades.Constantes;
import mx.unam.sistop.proyecto1.utilidades.Impresor;
import mx.unam.sistop.proyecto1.utilidades.Logger;

/**
 * Representa el Mostrador del establecimiento. Contendrá un cierto número de TrabajadoresEnMostrador, quienes se
 * encargarán de atender a los Clientes en la fila.
 */
public class Mostrador implements Logger {
    private final Fila fila;
    private final Horno horno;

    private Mostrador(Fila fila, Horno horno) {
        this.fila = fila;
        this.horno = horno;
    }

    public static void iniciar(Fila fila, Horno horno) {
        Mostrador mostrador = new Mostrador(fila, horno);
        mostrador.imprimirMensaje("Iniciando...");
        for (int i = 0; i < Constantes.TRABAJADORES_EN_MOSTRADOR; i++) {
            int id = i + 1;
            mostrador.imprimirMensaje("Creando e iniciando TrabajadorEnMostrador " + id + "...");
            new Thread(new TrabajadorEnMostrador(id, mostrador)).start();
        }
        mostrador.imprimirMensaje("Listo");
    }

    public void imprimirMensaje(String mensaje) {
        Impresor.imprimirRojo("Mostrador", mensaje);
    }

    public Cliente llamarCliente() {
        imprimirMensaje("Llamando al siguiente cliente en la fila");
        return fila.llamarAlPrimero();
    }

    public Pizza sacarPizzaListaDelHorno() {
        imprimirMensaje("Sacando pizza del horno...");
        return horno.sacarPizzaLista();
    }
}

// TODO: Añadir documentación y comentarios
