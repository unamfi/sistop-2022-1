package utilidades;

import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.Data;

import java.io.File;
import java.io.IOException;

@Data
public class Constantes {
    public static int MAX_CLIENTES_EN_PERIODO = 5;
    public static int TIEMPO_ENTRE_LLEGADA_DE_CLIENTES = 15;
    public static int MAX_PIZZAS_POR_CLIENTE = 5;
    //public static int MAX_PIZZAS_EN_INVENTARIO = 1000;
    public static int PIZZEROS = 3;
    public static int TIEMPO_PARA_PONER_PIZZA_EN_HORNO = 1;
    public static int MAX_PIZZAS_LISTAS = 15;
    public static int MAX_PIZZAS_HORNEANDOSE = 15;
    public static int TIEMPO_DE_HORNEADO = 10;
    public static int TRABAJADORES_EN_MOSTRADOR = 3;
    public static int TIEMPO_DE_PREPARACION_DE_PIZZA = 5;

    public static Constantes obtenerDeJson() {
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            return objectMapper.readValue(new File("constantes.json"), Constantes.class);
        } catch (IOException e) {
            throw new RuntimeException("No se pudo abrir el archivo de constantes", e);
        }
    }
}
