import java.util.ArrayList;

public class BlackJackHand extends Hand<BlackJackCard>{
    /* There are multiple possible scores for a blackjack hand, since aces have
     * multiple values. Return the highest possible score thats under 21, or
     * the lowest score that's over.
     */

    public int score() {
        ArraList<Integer> scores = possibleScores();
        int maxUnder = Integer.MIN_VALUE;
        int minOver = Integer.MAX_VALUE;

        for (int score : scores) {
            if (score > 21 && score < minOver) {
                minOver = score;
            } else if (score <= 21 && score > maxUnder) {
                maxUnder = score;
            }
        }
        return maxUnder == Integer.MIN_VALUE ? minOver : maxUnder;
    }

    /* REturn a list of all possible scores this hand could have
     * evaluating each ace as both 1 and 11
     */
    private ArrayList<Integer> possibleScores() { /* implemetnation here */ }

    public boolean busted() { return score() > 21; }
    public boolean is21() { return score() == 21; }
    public boolean isBlackHack() { /* Implementation here */ }
}
