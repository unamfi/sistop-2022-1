package mx.unam.sistop.tarea4;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class FileSystem {
    private static final Map<String, SimulatedFile> files = new HashMap<>();
    private static final Map<Integer, SimulatedFileDescriptor> fileDescriptors = new HashMap<>();

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

                case "open":
                    if (split.length == 3) handleOpen(split[1], split[2]);
                    else printUsage();
                    break;

                case "close":
                    if (split.length == 2) handleClose(split[1]);
                    else printUsage();
                    break;

                default:
                    printUsage();
            }
        }


    }

    private static void handleClose(String descriptor) {
        int descriptorId;
        try {
            descriptorId = Integer.parseInt(descriptor);
            if (descriptorId < 1) throw new NumberFormatException();
        } catch (NumberFormatException e) {
            System.err.println("Error: Formato de descriptor inválido (debe ser un entero positivo)");
            return;
        }

        if (!fileDescriptors.containsKey(descriptorId)) {
            System.err.println("Error: Descriptor inexistente");
            return;
        }

        fileDescriptors.remove(descriptorId);
        System.out.println("Descriptor " + descriptorId + " cerrado");
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
        files.put("arch1", new SimulatedFile("arch1",
                "012345678901234567890123456789012345678901234567890123456789"));

        files.put("arch2", new SimulatedFile("arch2",
                "432903249803432754832574897589437587349857349875983471"));

        files.put("helloworld", new SimulatedFile("helloworld",
                "320948325093428932617647812661464876fsdafasddasfdfsdasdf"));

        files.put("stgut.txt", new SimulatedFile("stgut.txt",
                "dasfdasofjnasdofjfdjoasioasfdafsd"));
    }

    private static void handleDir() {
        for (SimulatedFile file : files.values()) {
            System.out.print(file.getFilename() + " [" + file.getSize() + " bytes]\t");
        }
        System.out.println();
    }


    private static void handleOpen(String filename, String mode) {
        if (!files.containsKey(filename)) {
            System.err.println("Error: Archivo inexistente");
            return;
        }

        Mode modeEnum;
        switch (mode) {
            case "R":
                modeEnum = Mode.READ;
                break;
            case "A":
                modeEnum = Mode.READ_WRITE;
                break;
            case "W":
                modeEnum = Mode.WRITE;
                break;
            default:
                System.err.println("Error: El modo indicado es inválido");
                return;
        }


        SimulatedFileDescriptor fileDescriptor =
                new SimulatedFileDescriptor(SimulatedFileDescriptor.CURRENT_DESCRIPTOR_ID, modeEnum,
                        files.get(filename));
        SimulatedFileDescriptor.CURRENT_DESCRIPTOR_ID++;
        fileDescriptors.put(fileDescriptor.getId(), fileDescriptor);

        System.out.println("Archivo abierto (" + mode + ") → " + fileDescriptor.getId());
    }
}
