import utilidades.ColaSegura;

public class Fila {
    private final ColaSegura<Cliente> cola;

    public Fila() {
        this.cola = new ColaSegura<>(1000);
    }

    public void formarCliente(Cliente cliente) {
        this.cola.encolar(cliente);
    }

    public Cliente llamarAlPrimero() {
        return this.cola.desencolar();
    }
}
