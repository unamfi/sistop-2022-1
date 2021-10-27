package mx.unam.sistop.proyecto1.utilidades;

/**
 * Imprime mensajes de un actor, coloreando su nombre únicamente.
 */
public class Impresor {

    private static final String ANSI_RESET = "\u001B[0m";
    private static final String ANSI_NEGRO = "\u001B[30m";
    private static final String ANSI_ROJO = "\u001B[31m";
    private static final String ANSI_VERDE = "\u001B[32m";
    private static final String ANSI_AMARILLO = "\u001B[33m";
    private static final String ANSI_AZUL = "\u001B[34m";
    private static final String ANSI_MORADO = "\u001B[35m";
    private static final String ANSI_CIAN = "\u001B[36m";
    private static final String ANSI_BLANCO = "\u001B[37m";

    public static void imprimirNegro(String actor, String mensaje) {
        System.out.println(ANSI_NEGRO + "(" + actor + ") " + ANSI_RESET + mensaje);
    }

    public static void imprimirRojo(String actor, String mensaje) {
        System.out.println(ANSI_ROJO + "(" + actor + ") " + ANSI_RESET + mensaje);
    }

    public static void imprimirVerde(String actor, String mensaje) {
        System.out.println(ANSI_VERDE + "(" + actor + ") " + ANSI_RESET + mensaje);
    }

    public static void imprimirAmarillo(String actor, String mensaje) {
        System.out.println(ANSI_AMARILLO + "(" + actor + ") " + ANSI_RESET + mensaje);
    }

    public static void imprimirAzul(String actor, String mensaje) {
        System.out.println(ANSI_AZUL + "(" + actor + ") " + ANSI_RESET + mensaje);
    }

    public static void imprimirMorado(String actor, String mensaje) {
        System.out.println(ANSI_MORADO + "(" + actor + ") " + ANSI_RESET + mensaje);
    }

    public static void imprimirCian(String actor, String mensaje) {
        System.out.println(ANSI_CIAN + "(" + actor + ") " + ANSI_RESET + mensaje);
    }

    public static void imprimirBlanco(String actor, String mensaje) {
        System.out.println(ANSI_BLANCO + "(" + actor + ") " + ANSI_RESET + mensaje);
    }
}
