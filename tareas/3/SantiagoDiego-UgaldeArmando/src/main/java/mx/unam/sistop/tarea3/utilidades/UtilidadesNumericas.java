package mx.unam.sistop.tarea3.utilidades;

import java.util.Arrays;
import java.util.Random;

public class UtilidadesNumericas {
    public static int obtenerEnteroPositivoAleatorio(int max) {
        Random ran = new Random();
        return ran.nextInt(max) + 1;
    }

    public static int obtenerEnteroInclusivo(int min, int max) {
        Random ran = new Random();
        return ran.nextInt(max - min) + min;
    }

    public static double obtenerPromedio(double[] arr) {
        double total = Arrays.stream(arr).reduce(0, Double::sum);
        return total / arr.length;
    }
}