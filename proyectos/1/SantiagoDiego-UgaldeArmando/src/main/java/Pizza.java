public class Pizza {
    private final int id;
    private boolean cruda = true;

    public Pizza(int id) {
        this.id = id;
    }

    public void marcarComoHorneada() {
        cruda = false;
    }

    @Override
    public String toString() {
        return "pizza " + id;
    }
}
