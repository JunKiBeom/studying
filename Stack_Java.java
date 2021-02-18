interface Stack{
    boolean isEmpty();
    boolean isFull();
    void push(char item);
    char pop();
    char peek();
    void clear();
    void print();
}

class ArrayStack implements Stack {

    // private 변수 선언
    private int top;
    private int stackSize;
    private char stackArr[];

    // 생성자 선언부
    public ArrayStack(int stackSize) {
        top = -1; // 스택 포인터 초기화
        this.stackSize = stackSize; // 스택 사이즈 초기화
        stackArr = new char[this.stackSize]; // 스택 배열 생성
    }

    // method 선언

    // 스택이 비어있는지 확인
    public boolean isEmpty(){
        return (top==-1);
    }

    // 스택이 가득 찼는지 확인
    public boolean isFull() {
        return (top == this.stackSize-1);
    }

    // 스택에 데이터 추가
    public void push(char item) {
        if (isFull())
            System.out.println("Stack is Full");
        else {
            System.out.println("Push "+item);
            stackArr[++top] = item;
        }
    }

    // 스택에서 데이터 추출
    public char pop () {
        if (isEmpty()) {
            System.out.println("Stack is Empty");
            return 0;
        }
        else {
            System.out.println("Pop "+stackArr[top]);
            return stackArr[top--];
        }
    }

    // 스택 최상단 데이터 반환
    public char peek () {
        if (isEmpty()) {
            System.out.println("Stack is Empty");
            return 0;
        }
        else {
            System.out.println("Peek "+stackArr[top]);
            return stackArr[top];
        }
    }

    // 스택 초기화
    public void clear () {
        for (int i = 0; i < this.stackSize; i++)
            stackArr[i] = 0;
    }

    // 스택 내용 출력
    public void print() {
        if (isEmpty())
            System.out.println("Stack is Empty");
        else
            for (int i = 0; i <=top; i++)
                System.out.print(stackArr[i]+" ");
        System.out.println();
    }
}