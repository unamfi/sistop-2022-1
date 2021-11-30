package mx.unam.sistop.tarea4;

import java.util.HashSet;
import java.util.Set;

public class FileSystem {
    private static final Set<SimulatedFile> files = new HashSet<>();

    public static void main(String[] args) {
        initialize();
        handleDir();
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
