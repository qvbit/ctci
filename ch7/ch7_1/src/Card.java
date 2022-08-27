public abstract class Card {
    private boolean available = true;

    /* A number or face that's on the card: a number 2 through 10,
    or 11 for Jack, 12 for Queen, 13 for King, 1 for Ace */
    protected int faceValue;

    protected Suit suit;

    public Card(int c, Suit s) {
        faceValue = c;
        suit = s;
    }

    public abstract int value();
    public Suit suit() { return suit; }

    /* Check if card is available to be given to someone */
    public boolean isAvailable() { return available; }
    public void markUnavailable() { available = false; }
    public void markAvailable() { available = true; }
}
