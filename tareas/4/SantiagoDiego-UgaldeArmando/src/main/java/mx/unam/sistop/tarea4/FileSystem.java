package mx.unam.sistop.tarea4;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class FileSystem {
    private static final Set<SimulatedFile> files = new HashSet<>();

    public static void main(String[] args) {
        initialize();
        printUsage();

        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine().strip();
            String[] split = line.split(" ");

            if (split.length == 0 || split.length > 3) {
                printUsage();
                continue;
            }

            switch (split[0]) {
                case "dir":
                    if (split.length == 1) handleDir();
                    else printUsage();
                    break;

                case "quit":
                    if (split.length == 1) return;
                    else printUsage();
                    break;

                default:
                    printUsage();
            }
        }


    }

    private static void printUsage() {
        System.out.println("\nUso:");
        System.out.println("dir → Muestra el directorio");
        System.out.println("open <arch> <modo> → Especifica que operaremos con el archivo de nombre \"arch\", " +
                "empleando el modo especificado. Entrega un descriptor de archivo numérico.");
        System.out.println("close <descr> → Termina una sesión de trabajo con el archivo referido por el descriptor " +
                "indicado. Después de un close, cualquier intento por usar ese archivo entregará error.");
        System.out.println("read <descr> <longitud> → Lee la cantidad de bytes especificada");
        System.out.println("write <descr> <longitud> <datos» → Escribe la cantidad de bytes especificada, guardando " +
                "los datos indicados como parámetro.");
        System.out.println("seek <descr> <ubicacion> → Salta a la ubicación especificada del archivo");
        System.out.println("quit → Detiene la ejecucin de la simulación\n");
    }

    private static void initialize() {
        files.add(new SimulatedFile("arch1", "012345678901234567890123456789012345678901234567890123456789"));
        files.add(new SimulatedFile("arch2", "432903249803432754832574897589437587349857349875983471"));
        files.add(new SimulatedFile("helloworld", "320948325093428932617647812661464876fsdafasddasfdfsdasdf"));
        files.add(new SimulatedFile("stgut.txt", "dasfdasofjnasdofjfdjoasioasfdafsd"));
    }

    private static void handleDir() {
        for (SimulatedFile file : files) {
            System.out.print(file.getFilename() + " [" + file.getSize() + " bytes]\t");
        }
        System.out.println();
    }
}
