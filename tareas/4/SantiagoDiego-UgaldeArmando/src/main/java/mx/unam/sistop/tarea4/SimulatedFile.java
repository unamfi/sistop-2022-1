package mx.unam.sistop.tarea4;

import lombok.Value;

import java.util.ArrayList;
import java.util.List;

@Value
public class SimulatedFile {
    String filename;
    List<Character> data = new ArrayList<>();

    public SimulatedFile(String filename, String data) {
        this.filename = filename;
        for (char c : data.toCharArray()) this.data.add(c);
    }

    public int getSize() {
        return data.size();
    }
}
