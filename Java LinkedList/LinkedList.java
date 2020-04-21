public class LinkedList {
//여기에 링크드리스트 데이터, 동작들 정의! 
    //String [] data = new String[10];
    // 예시 . 배열 10개 할당 후 처음 공간에 data 저장
    // 최소한 고리의 시작점은 알려주어야 함(node 공간 하나 설정)
    static int size = 0;
    LinkedList()// 생성자 함수
    {
        Head = null;
    }
    //처음에 헤더가 없음

    private Node Head;

    public void insertFirst(String data) {
        Node newNode = new Node(data);
        newNode.next = Head;

        Head = newNode;
        size++;
    }

    public void print() { //출력 함수
        Node tail = Head;
        while(tail != null) {
            System.out.println(tail.getData());
            tail = tail.next;
        }
    }
    public void deleteLast() {
        // size--;
        //직접 만들기
        //맨 마지막 꼬리의 전 블럭 찾는것이 핵심. 그 노드의 next를 null로
    }
    public void deleteFirst() {
        Head = Head.next;
        size--;
    }
    //링크드리스트 맨 뒤에 새로운 데이터를 추가하는 함수
    public void insertLast(String data) { //함수가 내부적으로만 동작하고 끝낸다는 의미 : void. 리턴할 값이 없음을 의미
        //새로운 노드에 데이터 삽입
        Node newNode = null;
        newNode = new Node(data);

        if (Head ==null) {

            Head = newNode;
            size++;
        }
        else {

            //Node newNode = new Node(data);
            //마지막 노드 주소값이 새로운 노드를 가리키도록함

            //마지막 노드를 찾기!
            Node tail = Head;
            while(tail.next != null)
                tail = tail.next;

            tail.next = newNode;
            size++;
        }
    }
    public int getLength() {
        return size;
    }
}