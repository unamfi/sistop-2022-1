package mx.unam.sistop.tarea4;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class FileSystem {
    private static final Map<String, SimulatedFile> files = new HashMap<>();
    private static final Map<Integer, SimulatedFileDescriptor> fileDescriptors = new HashMap<>();

    public static void main(String[] args) {
        Util.initializeFiles(files);
        Util.printUsage();

        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine().strip();
            String[] split = line.split(" ");

            if (split.length == 0 || split.length > 4) {
                Util.printUsage();
                continue;
            }

            switch (split[0]) {
                case "dir":
                    if (split.length == 1) handleDir();
                    else Util.printUsage();
                    break;

                case "quit":
                    if (split.length == 1) return;
                    else Util.printUsage();
                    break;

                case "open":
                    if (split.length == 3) handleOpen(split[1], split[2]);
                    else Util.printUsage();
                    break;

                case "close":
                    if (split.length == 2) handleClose(split[1]);
                    else Util.printUsage();
                    break;

                case "read":
                    if (split.length == 3) handleRead(split[1], split[2]);
                    else Util.printUsage();
                    break;

                case "seek":
                    if (split.length == 3) handleSeek(split[1], split[2]);
                    else Util.printUsage();
                    break;

                case "write":
                    if (split.length == 4) handleWrite(split[1], split[2], split[3]);
                    else Util.printUsage();
                    break;

                default:
                    Util.printUsage();
            }
        }


    }

    private static void handleWrite(String descriptor, String lengthStr, String data) {
        int descriptorId = Util.parseDescriptor(descriptor, fileDescriptors);
        if (descriptorId == -1) return;

        SimulatedFileDescriptor fileDescriptor = fileDescriptors.get(descriptorId);

        if (fileDescriptor.getMode() != Mode.WRITE && fileDescriptor.getMode() != Mode.READ_WRITE) {
            System.err.println("Error: El archivo no se encuentra abierto para escritura");
            return;
        }

        int length = Util.parseLength(lengthStr);
        if (length == -1) return;

        if (data.length() != length) {
            System.err.println("Error: La longitud especificada no coincide con los datos a insertar");
            return;
        }

        int offset = fileDescriptor.getOffset();
        try {
            int newOffset = fileDescriptor.getFile().writeData(offset, data);
            fileDescriptor.setOffset(newOffset);
        } catch (IndexOutOfBoundsException e) {
            System.err.println("Error: El índice especificado se encuentra fuera de los límites del archivo");
            return;
        }

        System.out.println("Escritura exitosa");
    }

    private static void handleSeek(String descriptor, String offset) {
        int descriptorId = Util.parseDescriptor(descriptor, fileDescriptors);
        if (descriptorId == -1) return;

        SimulatedFileDescriptor fileDescriptor = fileDescriptors.get(descriptorId);

        int newOffset = Util.parseNonnegativeInteger(offset,
                "Error: Formato de offset inválido (debe ser un entero no negativo)");

        fileDescriptor.setOffset(newOffset);
        System.out.println("Nueva posición del descriptor: " + newOffset);
    }

    private static void handleRead(String descriptor, String lengthStr) {
        int descriptorId = Util.parseDescriptor(descriptor, fileDescriptors);
        if (descriptorId == -1) return;

        SimulatedFileDescriptor fileDescriptor = fileDescriptors.get(descriptorId);

        if (fileDescriptor.getMode() == Mode.WRITE) {
            System.err.println("Error: El archivo no se encuentra abierto para lectura");
            return;
        }

        int length = Util.parseLength(lengthStr);
        if (length == -1) return;

        int offset = fileDescriptor.getOffset();
        String readData;
        try {
            SimulatedFile file = fileDescriptor.getFile();
            readData = file.getFileData(offset, length);
            int newOffset = offset + length;
            fileDescriptor.setOffset(Math.min(newOffset, file.getSize()));
        } catch (IndexOutOfBoundsException e) {
            System.err.println("Error: El índice especificado se encuentra fuera de los límites del archivo");
            return;
        }

        System.out.println(readData);
    }

    private static void handleClose(String descriptor) {
        int descriptorId = Util.parseDescriptor(descriptor, fileDescriptors);
        if (descriptorId == -1) return;

        fileDescriptors.remove(descriptorId);
        System.out.println("Descriptor " + descriptorId + " cerrado");
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
                files.get(filename).deleteContents();
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
