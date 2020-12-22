class Apple {
    public String toString() {return "I am an apple.";}
}

class Orange {
    public String toString() {return "I am an orange.";}
}

// 다음 상자는 사과도 오랜지도 담을 수 있다.
class Box{  // 무엇이든 저장하고 꺼낼 수 있는 상자
    private Object ob;

    public void set(Object o) {ob=o;}
    public Object get() {return ob;}
}

class Box2<T> {
    private T ob;

    public void set(T o) {
        ob = o;
    }
    public T get() {
        return ob;
    }
}

public class Generics {
    public static void main(String[] args) {
        Box aBox = new Box();   // 상자 생성
        Box oBox = new Box();   // 상자 생성

        aBox.set(new Apple());  // 사과를 상자에 담는다
        oBox.set(new Orange()); // 오렌지를 상자에 담는다

        Apple ap = (Apple)aBox.get();   // 상자에서 사과를 꺼낸다
        Orange og = (Orange)oBox.get(); // 상자에서 오렌지를 꺼낸다

        System.out.println(ap);
        System.out.println(og);

        /*
        어쩔 수 없이 형 변환이 과정이 수반된다.
        그릐고 이는 컴파일러의 오류 발견 가능성을 낮추는 결과로 이어짐
        */


        // 다음 두 문장은 프로그래머의 실수
        aBox.set("Apple");
        oBox.set("Orange");

        System.out.println(aBox.get());
        System.out.println(oBox.get());

        Box2<Apple> aBox2 = new Box2<Apple>();  // T를 Apple로 결정
        Box2<Orange> oBox2 = new Box2<Orange>();    // T를 Orange로 결정

        aBox2.set(new Apple());     // 사과를 상자에 담는다
        oBox2.set(new Orange());    // 오렌지를 상자에 담는다

        Apple ap2 = aBox2.get();    // 사과를 꺼내는데 형변환x
        Orange og2 = oBox2.get();   // 오렌지를 꺼내는데 형변환x

        System.out.println(ap2);
        System.out.println(og2);

        /*
        aBox2.set("Apple");
        oBox2.set("Orange");
        실수가 컴파일 에러로 넘어감
         */
    }
}

