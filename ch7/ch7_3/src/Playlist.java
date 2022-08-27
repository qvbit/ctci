/**
 * The Playlist manages the current and next songs to play. It is essentially a wrapper class for a
 * queue and offers some additional methods for convenience.
 */
public class Playlist {
    private Song song;
    private Queue<Song> queue;

    public Playlist(Song song, Queue<Song> queue) {
        this.song = song;
        this.queue = queue;
    }

    public Song getNextSToPlay() {
        // Personal note: Shouldn't we also remove the song? Otherwise next song is always the the head of queue.
        return queue.peek();
    }

    public void queueUpSong(Song s) {
        queue.add(s);
    }
}
