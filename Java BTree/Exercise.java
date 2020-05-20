package tree;

public class Exercise {
    public static void main(String[] args) {
        Tree tree = new Tree();
        tree.insert(31);
        tree.insert(16);
        tree.insert(45);
        tree.insert(24);
        tree.insert(7);
        tree.insert(19);
        tree.insert(29);

        tree.traverse();
    }
}
