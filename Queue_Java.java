interface Queue {
    boolean isEmpty();
    boolean isFull();
    void enqueue(char item);
    char dequeue();
    char peek();
    char bottom();
    void clear();
    void print();
}

class ArrayQueue implements Queue {
    // private 변수 선언
    private int front;
    private int rear;
    private int queueSize;
    private char queueArr[];

    // 생성자 선언부
    public ArrayQueue(int QueueSize) {
        front = -1; // 큐 포인터 초기화
        rear = -1;
        this.queueSize = QueueSize; // 큐 사이즈 초기화
        queueArr = new char[this.queueSize]; // 큐 배열 생성
    }

    // method 선언

    // 큐가 비어있는지 확인
    public boolean isEmpty(){
        return (front==rear);
    }

    // 큐가 가득 찼는지 확인
    public boolean isFull() {
        return (rear == this.queueSize-1);
    }

    // 큐에 데이터 추가
    public void enqueue(char item) {
        if (isFull())
            System.out.println("Queue is Full");
        else {
//            System.out.println("Push "+item);
            queueArr[++rear] = item;
        }
    }

    // 큐에서 데이터 추출
    public char dequeue() {

        if (isEmpty()) {
            System.out.println("Queue is Empty");
            return 0;
        }
        else {
            char tmp = queueArr[++front];
            for (int i=0;i<this.queueSize-1;i++) {
                queueArr[i]=queueArr[i+1];
            }
            front--; rear--;
            return tmp;
        }
    }

    // 큐의 최상단 데이터 반환
    public char peek () {
        if (isEmpty()) {
            System.out.println("Queue is Empty");
            return 0;
        }
        else {
//            System.out.println("Peek "+QueueArr[rear]);
            return queueArr[rear];
        }
    }

    // 큐의 최하단 데이터 반환
    public char bottom () {
        if (isEmpty()) {
            System.out.println("Queue is Empty");
            return 0;
        }
        else {
//            System.out.println("Peek "+QueueArr[front++]);
            return queueArr[++front];
        }
    }

    // 큐 초기화
    public void clear() {
        for (int i = 0; i < this.queueSize; i++)
            queueArr[i] = 0;
        front=-1; rear=-1;
    }

    //  큐 내용 출력
    public void print() {
        if (isEmpty())
            System.out.print("Queue is Empty");
        else
            for (int i = 0; i <=rear; i++)
                System.out.print(queueArr[i]+" ");
        System.out.println();
    }

}