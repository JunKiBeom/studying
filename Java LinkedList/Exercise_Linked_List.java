public class Exercise_Linked_List {
    //링크드 리스트 구현
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        LinkedList list = new LinkedList();

        list.insertLast("A");
        list.insertLast("B");
        list.insertLast("C");
        list.insertLast("D");

        list.insertFirst("Z");
        list.deleteFirst();
        list.print();
        System.out.println(list.getLength());
    }

}