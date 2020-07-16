public class Exercise_Linked_List {
    //링크드 리스트 구현
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        LinkedList a = new LinkedList();
        LinkedList b = new LinkedList();

        a.insert("1");
        a.insert("2");
        b.insert("a");
        b.insert("b");
        b.insert("c");
        a.merge(b);
        a.print();
        System.out.println(a.getLength());
    }

}