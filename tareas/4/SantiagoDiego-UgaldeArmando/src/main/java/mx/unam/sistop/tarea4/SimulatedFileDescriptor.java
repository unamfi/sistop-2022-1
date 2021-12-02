package mx.unam.sistop.tarea4;

import lombok.Data;

@Data
public class SimulatedFileDescriptor {
    public static int CURRENT_DESCRIPTOR_ID = 1;
    private final int id;
    private final Mode mode;
    private final SimulatedFile file;
    private int offset = 0;
}
