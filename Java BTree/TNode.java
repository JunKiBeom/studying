package tree;

public class TNode {
    public TNode left;
    public TNode right;

    private int data;

    TNode(int input) {
        data = input;
    }

    public int getData() {
        return data;
    }
}
