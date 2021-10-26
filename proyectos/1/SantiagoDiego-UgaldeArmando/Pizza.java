public class Pizza {
    private final int id;
    private boolean cruda = true;

    public Pizza(int id) {
        this.id = id;
    }

    public void marcarComoHorneada() {
        cruda = true;
    }

    @Override
    public String toString() {
        return "Pizza número " + id;
    }
}
