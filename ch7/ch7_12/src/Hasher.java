import java.util.ArrayList;

public class Hasher<K, V> {
    /* Linked list node class. Used only within hash table. No one else should get
     * access to this. Implemented as a double linked list
     */
    private static class LinkedListNode<K, V> {
        public LinkedListNode<K, V> next;
        public LinkedListNode<K, V> prev;
        public K key;
        public V value;

        public LinkedListNode(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }

    private ArrayList<LinkedListNode<K, V>> arr;
    public Hasher(int capacity) {
        /* Create list of linked lists at a particular size. FIll list with null values,
         * as its the only way to make the array the desired size */
        arr = new ArrayList<>();
        arr.ensureCapacity(capacity);  // Optional optimization
        for (int i = 0; i < capacity; i++) {
            arr.add(null);
        }
    }

    /* Insert key and value into the hash table */
    public void put(K key, V value) {
        LinkedListNode<K, V> node = getNodeForKey(key);
        if (node != null) {  // If node is already exists
            node.value = value;  // Just update the value of existing node
            return;
        }

        // Else we create the new node
        node = new LinkedListNode<>(key, value);
        int index = getIndexForKey(key);
        if (arr.get(index) != null) {  // If collision
            node.next = arr.get(index);
            node.next.prev = node;
        }
        arr.set(index, node);  // Note that node always becomes new head of the LL at index. arr.set sets head
    }

    /* Remove node for key */
    public void remove(K key) {
        LinkedListNode<K, V> node = getNodeForKey(key);
        /* First fix to the left of the node */
        if (node.prev != null) {
            node.prev.next = node.next;
        } else {
            /* Removing head => update */
            int hashKey = getIndexForKey(key);
            arr.set(hashKey, node.next);  // arr.set the head
        }

        /* Next fix to the right */
        if (node.next != null) {
            node.next.prev = node.prev;
        }
    }

    /* Get value for key */
    public V get(K key) {
        LinkedListNode<K, V> node = getNodeForKey(key);
        return node == null ? null : node.value;
    }

    /* Get LL node associated with given key */
    private LinkedListNode<K, V> getNodeForKey(K key) {
        int index = getIndexForKey(key);  // This is the hash function
        LinkedListNode<K, V> current = arr.get(index);

        while(current != null) {
            if (current.key == key) {
                return current;
            }
            current = current.next;
        }
        return null;  // Did not find key in hash table
    }

    /* Really naive hash function to map a key to an index */
    public int getIndexForKey(K key) {
        return Math.abs(key.hashCode() % arr.size());
    }
}
