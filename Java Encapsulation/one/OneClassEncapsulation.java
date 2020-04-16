package one; // 적절한 캡슐화의 예 (가정 : 코감기는 콧물, 재채기, 코 막힘을 늘 동반한다.)

class SinusCap {
    void sniTake(){
        System.out.println("콧물이 싹 납니다.");
    }
    void sneTake(){
        System.out.println("재채기가 멎습니다.");
    }
    void snuTake(){
        System.out.println("코가 뻥 뚫립니다.");
    }
    void take() { // 약의 복용 방법 및 순서가 담긴 메소드
        sniTake();
        sneTake();
        snuTake();
    }
}

// -- 포함 관계로 캡슐화 완성하기
class SinivelCap { // 콧물 처치용 캡술
    void take(){
        System.out.println("콧물이 싹 납니다.");
    }
}

class SneezeCap { // 재채기 처치용 캡술
    void take(){
        System.out.println("재채기가 멎습니다.");
    }
}

class SnuffleCap { // 코 막힘 처치용 캡술
    void take(){
        System.out.println("코가 뻥 뚫립니다.");
    }
}

class SinusCap2 {
    SinivelCap siCap = new SinivelCap();
    SneezeCap szCap = new SneezeCap();
    SnuffleCap sfCap = new SnuffleCap();

    void take() {
        siCap.take(); szCap.take(); sfCap.take();
    }
}
// -- 완성

class ColdPatient {  // 환자 약 복용
    void takeSinus(SinusCap cap) {
        cap.take();
    }
    void takeSinus2(SinusCap2 cap) {
        System.out.println("\nSinusCap 2");
        cap.take();
    }
}

class OneClassEncapsulation {
    public static void main(String[] args) {
        ColdPatient suf = new ColdPatient();
        suf.takeSinus(new SinusCap());
        suf.takeSinus2(new SinusCap2());
    }
}
/*
코감기 관련해서 알아야 할 사실들이 많이 줄었다.
SnivelCap, SneezeCap, SnuffleCap클래스들은 몰라도 된다.
SniusCap클래스 하나만 알면 된다.
복용 순서 몰라도 된다. take메소드를 통해 복용과정이 모두 자동화 된다.
 */