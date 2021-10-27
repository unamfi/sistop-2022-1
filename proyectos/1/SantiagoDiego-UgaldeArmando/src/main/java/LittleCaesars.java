import utilidades.Constantes;

public class LittleCaesars {
    public static void main(String[] args) {
        // TODO: Añadir variable de condición para detener operaciones.

        // Inicializar constantes importantes
        Constantes.obtenerDeJson();
        System.out.println("¡Little Caesars inicia sus operaciones!");

        // Fila y horno serán recursos que se comparten por los productores y consumidores
        Fila fila = new Fila();
        Horno horno = new Horno();

        // Iniciar productores y consumidores proporcionando las dependencias necesarias
        Calle.iniciar(fila);
        Cocina.iniciar(horno);
        Mostrador.iniciar(fila, horno);
    }
}
