public class Fila {
    private final ColaSegura<Cliente> cola;

    public Fila() {
        this.cola = new ColaSegura<>(Integer.MAX_VALUE);
    }

    private void formarCliente(Cliente cliente) {
        this.cola.encolar(cliente);
    }

    private Cliente llamarAlPrimero() {
        return this.cola.desencolar();
    }
}
