package mx.unam.sistop.tarea4;

import lombok.Data;

@Data
public class FileDescriptor {
    private final int id;
    private final Mode mode;
    private final SimulatedFile file;
    private int offset;
}
