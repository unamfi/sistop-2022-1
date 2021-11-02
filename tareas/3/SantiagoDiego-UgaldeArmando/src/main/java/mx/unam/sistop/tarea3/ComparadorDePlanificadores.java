package mx.unam.sistop.tarea3;

public class ComparadorDePlanificadores {
    private static final int RONDAS = 5;

    public static void main(String[] args) {
        for (int i = 0; i < RONDAS; i++) {
            System.out.println("Ronda " + (i + 1) + ":");
            Planificadores.ejecutar(CargaAleatoria.generar());
            System.out.println();
        }
    }
}
