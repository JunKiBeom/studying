class Singleton {
    private static Singleton one;   // static 변수 선언
    private Singleton() {
    }

    public static Singleton getInstance() {
        if(one==null) {             // one의 값이 null인 경우에만 객체를 생성하도록 함. *1회성 호출
            one = new Singleton();  // one 객체 단 한번만 생성됨, static 변수이므로 유지됨
        }
        return one;
    }
}

public class SingletonTest {
    public static void main(String[] args) {
        Singleton singleton1 = Singleton.getInstance();
        Singleton singleton2 = Singleton.getInstance();
        System.out.println(singleton1 == singleton2);
    }
}