import utilidades.ColaSegura;
import utilidades.Impresor;
import utilidades.Logger;

/**
 * Representa la fila para ser atendido en el establecimiento y funcionará como un buffer infinito. Los clientes serán
 * agregados por la Calle cada cierto tiempo y el primero será llamado por los TrabajadoresEnMostrador cada vez que
 * éstos estén libres para ser atendido.
 */
public class Fila implements Logger {
    private final ColaSegura<Cliente> cola;

    // Se considera a 1000 como un valor práctico para una fila "infinita".
    public Fila() {
        this.cola = new ColaSegura<>(1000);
    }

    public void imprimirMensaje(String mensaje) {
        Impresor.imprimirCian("Fila", mensaje);
    }

    public void formarCliente(Cliente cliente) {
        imprimirMensaje("El " + cliente + " se está formando");
        this.cola.encolar(cliente);
    }

    public Cliente llamarAlPrimero() {
        Cliente cliente = this.cola.desencolar();
        imprimirMensaje("El " + cliente + " ha sido llamado");
        return cliente;
    }
}