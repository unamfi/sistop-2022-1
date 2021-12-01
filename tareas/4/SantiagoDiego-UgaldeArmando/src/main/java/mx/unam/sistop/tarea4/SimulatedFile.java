package mx.unam.sistop.tarea4;

import lombok.Value;

@Value
public class SimulatedFile {
    String filename;
    StringBuilder fileData;

    public SimulatedFile(String filename, String data) {
        this.filename = filename;
        this.fileData = new StringBuilder(data);
    }

    public int getSize() {
        return fileData.length();
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
    public String getFileData(int offset, int length) throws IndexOutOfBoundsException {
        int fileLength = this.fileData.length();
        if (offset >= fileLength) throw new IndexOutOfBoundsException();
        return this.fileData.substring(offset, Math.min(fileLength, offset + length));
    }

    public int writeData(int offset, String newData) {
        int fileLength = this.fileData.length();
        int newDataLength = newData.length();

        offset = Math.min(offset, fileLength);

        int j = 0;
        for (int i = offset; i < fileLength; i++) {
            this.fileData.setCharAt(i, newData.charAt(j++));
            if (j == newDataLength) return i + 1;
        }

        for (; j < newDataLength; j++) {
            this.fileData.append(newData.charAt(j));
        }
        return this.fileData.length();
    }

    public void deleteContents() {
        this.fileData.setLength(0);
    }
}
