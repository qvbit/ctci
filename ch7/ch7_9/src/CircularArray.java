import org.w3c.dom.ls.LSOutput;

import java.util.Iterator;

public class CircularArray<T> implements Iterable<T>{
    private T[] items;
    private int head = 0;

    /* Constructor */
    public CircularArray(int size) {
        items = (T[]) new Object[size];
    }

    /* This gets the corresponding index of current items array (having possible had rotations applied)
     * but does not actually perform the rotation
     * despite having the logic to do so. Thats handled by the rotate function. */
    private int convert(int index) {
        if (index < 0) {
            index += items.length;
        }
        return (head + index) % items.length;
    }

    /* Does the actual rotation and sets the new head */
    public void rotate(int shiftRight) {
        head = convert(shiftRight);
    }

    public T get(int i) {
        if (i < 0 || i >= items.length) {
            throw new java.lang.ArrayIndexOutOfBoundsException("Out of bounds");
        }
        return items[convert(i)];  // Note that this doesnt change head/rotate array, it simply virtually indexes the rotated array
    }

    public void set(int i, T item) {
        items[convert(i)] = item;
    }

    public Iterator<T> iterator() {
        return new CircularArrayIterator<T>(this);
    }

    /* Nest the iterator class within */
    private class CircularArrayIterator<TI> implements Iterator<TI>{
        /* current reflects the offset from the rotated head, not from the actual start of the raw array */
        private int _current = -1;
        private TI[] _items;

        // Constructor
        public CircularArrayIterator(CircularArray<TI> array) {
            _items = array.items;
        }

        @Override
        public boolean hasNext() {
            return _current < items.length - 1;
        }

        @Override
        public TI next() {
            _current++;
            TI item = (TI) _items[convert(_current)];
            return item;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException("Can't remove items in this implementation, sorry..");
        }
    }
}
