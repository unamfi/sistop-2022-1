public class LittleCaesars {
    public static void main(String[] args) {
        // TODO: Añadir variable de condición para detener operaciones.
        // TODO: Añadir impresión de acciones.
        Fila fila = new Fila();
        Horno horno = new Horno();
        Calle.iniciar(fila);
        Cocina.iniciar(horno);
    }
}
