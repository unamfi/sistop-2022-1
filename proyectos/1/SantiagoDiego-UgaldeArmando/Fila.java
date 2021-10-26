import utilidades.ColaSegura;
import utilidades.Impresor;

public class Fila {
    private final ColaSegura<Cliente> cola;

    public Fila() {
        this.cola = new ColaSegura<>(1000);
    }

    private static void imprimirMensaje(String mensaje) {
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
// TODO: Agregar interfaz para imprimirMensaje