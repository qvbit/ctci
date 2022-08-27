/* Jukebox class represents the body of the problem. Many of the interactions between components
 * of the system, or between the user and the system are channelled through here.
 */
public class Jukebox {
    private CDPlayer cdPlayer;
    private User user;
    private Set<CD> cdCollection;
    private SongSelector ts;

    public Jukebox(CDPlayer cdPlayer, User user, Set<CD> cdCollection, SongSelector ts) {
        /* ... */
    }

    public Song getCurrentSong() { return ts.getCurrentSong(); }
    public void setUser(User u) { this.user = u; }
}
