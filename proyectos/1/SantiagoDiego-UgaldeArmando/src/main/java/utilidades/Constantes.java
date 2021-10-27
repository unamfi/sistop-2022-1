package utilidades;

import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.Data;

import java.io.File;
import java.io.IOException;

/**
 * Parámetros importantes del programa. Los valores se obtienen de un archivo JSON con los nombres de los parámetros en
 * minúsculas, como se muestra en los atributos de la clase. Si este archivo no se encuentra o no es posible abrirlo, se
 * utilizarán los valores por default. Además, todos los atributos son opcionales en el archivo, por lo que, de no
 * encontrarse alguno, se utilizará también su valor por default. Todos los tiempos se encuentran en segundos.
 */
@Data
public class Constantes {
    public static int MAX_CLIENTES_EN_PERIODO = 4;
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

    private int max_clientes_en_periodo = 5;
    private int tiempo_entre_llegada_de_clientes = 15;
    private int max_pizzas_por_cliente = 5;
    private int pizzeros = 3;
    private int tiempo_para_poner_pizza_en_horno = 1;
    private int max_pizzas_listas = 15;
    private int max_pizzas_horneandose = 15;
    private int tiempo_de_horneado = 10;
    private int trabajadores_en_mostrador = 3;
    private int tiempo_de_preparacion_de_pizza = 5;

    public static void obtenerDeJson() {
        ObjectMapper objectMapper = new ObjectMapper();
        Constantes constantes;
        try {
            constantes = objectMapper.readValue(new File("constantes.json"), Constantes.class);
        } catch (IOException e) {
            System.out.println("No se pudo abrir el archivo de constantes, utilizando valores por default.");
            Constantes.imprimir();
            return;
        }

        MAX_CLIENTES_EN_PERIODO = constantes.getMax_clientes_en_periodo();
        TIEMPO_ENTRE_LLEGADA_DE_CLIENTES = constantes.getTiempo_entre_llegada_de_clientes();
        MAX_PIZZAS_POR_CLIENTE = constantes.getMax_pizzas_por_cliente();
        PIZZEROS = constantes.getPizzeros();
        TIEMPO_PARA_PONER_PIZZA_EN_HORNO = constantes.getTiempo_para_poner_pizza_en_horno();
        MAX_PIZZAS_LISTAS = constantes.getMax_pizzas_listas();
        MAX_PIZZAS_HORNEANDOSE = constantes.getMax_pizzas_horneandose();
        TIEMPO_DE_HORNEADO = constantes.getTiempo_de_horneado();
        TRABAJADORES_EN_MOSTRADOR = constantes.getTrabajadores_en_mostrador();
        TIEMPO_DE_PREPARACION_DE_PIZZA = constantes.getTiempo_de_preparacion_de_pizza();

        Constantes.imprimir();
    }

    public static void imprimir() {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("MAX_CLIENTES_EN_PERIODO = ").append(MAX_CLIENTES_EN_PERIODO).append("\n");
        stringBuilder.append("TIEMPO_ENTRE_LLEGADA_DE_CLIENTES = ").append(TIEMPO_ENTRE_LLEGADA_DE_CLIENTES).append("\n");
        stringBuilder.append("MAX_PIZZAS_POR_CLIENTE = ").append(MAX_PIZZAS_POR_CLIENTE).append("\n");
        stringBuilder.append("PIZZEROS = ").append(PIZZEROS).append("\n");
        stringBuilder.append("TIEMPO_PARA_PONER_PIZZA_EN_HORNO = ").append(MAX_PIZZAS_LISTAS).append("\n");
        stringBuilder.append("MAX_PIZZAS_LISTAS = ").append(MAX_PIZZAS_LISTAS).append("\n");
        stringBuilder.append("MAX_PIZZAS_HORNEANDOSE = ").append(MAX_PIZZAS_HORNEANDOSE).append("\n");
        stringBuilder.append("TIEMPO_DE_HORNEADO = ").append(TIEMPO_DE_HORNEADO).append("\n");
        stringBuilder.append("TRABAJADORES_EN_MOSTRADOR = ").append(TRABAJADORES_EN_MOSTRADOR).append("\n");
        stringBuilder.append("TIEMPO_DE_PREPARACION_DE_PIZZA = ").append(TIEMPO_DE_PREPARACION_DE_PIZZA).append("\n");
        System.out.println(stringBuilder);
    }
}
