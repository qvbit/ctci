import java.util.LinkedList;

class AnimalQueue {
    LinkedList<Dog> dogs = new LinkedList<>();
    LinkedList<Cat> cats = new LinkedList<>();
    private int order = 0;

    public void enqueue(Animal a) {
        a.setOrder(order);
        order++;

        if (a instanceof Dog) dogs.add((Dog)a);
        else if (a instanceof Cat) cats.add((Cat)a);
    }

    public Dog dequeueDog() {
        return dogs.poll();
    }

    public Cat dequeueCat() {
        return cats.poll();
    }

    public Animal dequeueAny() {
        if (dogs.size() == 0) {
            return dequeueCat();
        } else if (cats.size() == 0) {
            return dequeueDog();
        }

        if (dogs.peek().compareTo(cats.peek()) > 0) {
            return dequeueDog();
        } else {
            return dequeueCat();
        }
    }
}

abstract class Animal implements Comparable<Animal>{
    private int order;
    protected String name;
    public Animal(String n) { name = n; }
    public void setOrder(int ord) { order = ord; }
    public int getOrder() { return order; }

    @Override
    public int compareTo(Animal o) {
        if (this.order < o.order) {
            return 1;
        } else if (this.order > o.order) {
            return -1;
        } else {
            return 0;
        }
    }
}

class Dog extends Animal {
    public Dog(String n) { super(n); }
}

class Cat extends Animal {
    public Cat(String n) { super(n); }
}
