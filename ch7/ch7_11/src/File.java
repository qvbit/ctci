public class File extends Entry{
    private String content;
    private int size;

    public File(Directory p, String n, int size) {
        super(p, n);
        this.size = size;
    }

    public int size() { return size; }
    public String getContents() { return content; }
    public void setContents(String c) { content = c; }
}
