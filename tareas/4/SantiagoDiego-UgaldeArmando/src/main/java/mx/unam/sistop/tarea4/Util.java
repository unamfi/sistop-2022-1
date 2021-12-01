package mx.unam.sistop.tarea4;

import java.util.Map;

public class Util {
    static int parseNonnegativeInteger(String number, String errorMessage) {
        try {
            int nonnegativeInt = Integer.parseInt(number);
            if (nonnegativeInt < 0) throw new NumberFormatException();
            return nonnegativeInt;
        } catch (NumberFormatException e) {
            System.err.println(errorMessage);
            return -1;
        }
    }

    static void printUsage() {
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

    static void initializeFiles(Map<String, SimulatedFile> files) {
        files.put("arch1", new SimulatedFile("arch1",
                "012345678901234567890123456789012345678901234567890123456789"));

        files.put("arch2", new SimulatedFile("arch2",
                "432903249803432754832574897589437587349857349875983471"));

        files.put("helloworld", new SimulatedFile("helloworld",
                "320948325093428932617647812661464876fsdafasddasfdfsdasdf"));

        files.put("stgut.txt", new SimulatedFile("stgut.txt",
                "dasfdasofjnasdofjfdjoasioasfdafsd"));
    }

    static int parseDescriptor(String descriptor, Map<Integer, SimulatedFileDescriptor> descriptorsMap) {
        int descriptorId = parseNonnegativeInteger(descriptor,
                "Error: Formato de descriptor inválido (debe ser un entero no negativo)");
        if (descriptorId == -1) return -1;

        if (!descriptorsMap.containsKey(descriptorId)) {
            System.err.println("Error: Descriptor inexistente");
            return -1;
        }

        return descriptorId;
    }

    static int parseLength(String length) {
        return parseNonnegativeInteger(length, "Error: Formato de longitud inválido (debe ser un entero no " +
                "negativo)");
    }
}
