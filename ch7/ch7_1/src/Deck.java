import java.util.ArrayList;

/* Takes a generic type that is constrained to be a type of Card */
public class Deck <T extends Card> {
    private ArrayList<T> cards;  // All cards, dealt or not
    private int dealtIndex = 0;  // Marks first undealt card

    public void setDeckOfCards(ArrayList<T> deckOfCards) { /* insert implementation here */ }

    public void shuffle() { /* implementation here */ }

    public int remainingCards() {
        return cards.size() - dealtIndex;
    }

    public T[] dealHand(int number) { /* implementation here */ }
    public T dealCard() { /* implementation here */ }
}
