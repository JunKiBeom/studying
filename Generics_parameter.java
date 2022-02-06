// '매개변수화 타입'을 '티입 인자'로 전달

class Box<T> {
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
        Box<String> sBox = new Box<>();
        sBox.set("I am so happy.");

        Box<Box<String>> wBox = new Box<>();
        wBox.set(sBox);

        Box<Box<Box<String>>> zBox = new Box<>();
        zBox.set(wBox);

        System.out.println(zBox.get().get().get());
//        zBox.get() -> wBox
//        zBox.get().get() -> sBox
//        zBox.get().get().get() -> sBox.get()
    }
}