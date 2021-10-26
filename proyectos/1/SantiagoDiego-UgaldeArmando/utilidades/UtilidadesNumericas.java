package utilidades;

import java.util.Random;

public class UtilidadesNumericas {
    public static int obtenerEnteroPositivoAleatorio(int max) {
        Random ran = new Random();
        return ran.nextInt(max) + 1;
    }
}
