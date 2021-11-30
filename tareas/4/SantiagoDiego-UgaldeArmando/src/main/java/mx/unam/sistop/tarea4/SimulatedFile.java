package mx.unam.sistop.tarea4;

import lombok.Value;

@Value
public class SimulatedFile {
    String filename;
    StringBuilder data;

    public SimulatedFile(String filename, String data) {
        this.filename = filename;
        this.data = new StringBuilder(data);
    }

    public int getSize() {
        return data.length();
    }

    /**
     * Reads the specified chunk of this file, starting with index <code>offset</code> and reading the specified number
     * of bytes. If <code>length</code> would cause the end index to surpass the file's bound, only the remaining bytes
     * will be returned.
     *
     * @param offset Chunk's start index
     * @param length Number of bytes to read
     * @return The specified chunk of data
     * @throws IndexOutOfBoundsException If the offset (start index) is greater than the file's bound.
     */
    public String getData(int offset, int length) throws IndexOutOfBoundsException {
        int dataLength = this.data.length();
        if (offset >= dataLength) throw new IndexOutOfBoundsException();
        return this.data.substring(offset, Math.min(dataLength, offset + length));
    }
}
