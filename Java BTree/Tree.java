package tree;

public class Tree {
    private TNode root;
    public Tree() {
        root = null;
    }
    public void insert(int data) {
        TNode node = new TNode(data);
        if(root == null) {
            root = node;
            return;
        }
        insertNode(root,node);
    }

    public void insertNode(TNode current, TNode node) {
        if (current.getData() > node.getData()) {
            if (current.left == null)
                current.left = node;
            else
                insertNode(current.left,node);
        }
        else {
            if (current.right == null)
                current.right = node;
            else
                insertNode(current.right,node);
        }
    }


    public boolean find(int data) {
        return true;
    }

    public void traverse() {
        System.out.println("Pre-order");
        traverse_preorder(root);
        System.out.println("In-order");
        traverse_inorder(root);
    }

    private void traverse_preorder(TNode cur) {
        if (cur == null)
            return;

        System.out.println(cur.getData());
        traverse_preorder(cur.left);
        traverse_preorder(cur.right);
    }

    private void traverse_inorder(TNode cur) {
        if (cur == null)
            return;
        traverse_inorder(cur.left);
        System.out.println(cur.getData());
        traverse_inorder(cur.right);
    }
}
