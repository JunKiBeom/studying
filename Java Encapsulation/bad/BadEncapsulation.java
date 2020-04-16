package bad;// 캡슐화의 무너진 예 (가정 : 코감기는 콧물, 재채기, 코 막힘을 늘 동반한다.)

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

class ColdPatient {  // 환자 약 복용
    void takeSinivelCap(SinivelCap cap) {
        cap.take();
    }
    void takeSneezeCap(SneezeCap cap) {
        cap.take();
    }
    void takeSnuffleCap(SnuffleCap cap) {
        cap.take();
    }
}

class BadEncapsulation { // 무너진 캡슐화 결과, 잘못된 캡슐화
    public static void main(String[] args) {
        ColdPatient suf = new ColdPatient();

        // 콧물 캡슐 구매 후 복용
        suf.takeSinivelCap(new SinivelCap());

        // 재채기 캡슐 구매 후 복용
        suf.takeSneezeCap(new SneezeCap());

        // 코막힘 캡슐 구매 후 복용
        suf.takeSnuffleCap(new SnuffleCap());
    }
}
/*
캡술화가 무너지면 이렇듯 클래스 사용 방법과 관련하여 알아야 할 사항들이 많이 등장한다.
- 복용해야 할 약의 종류
- 복용해야 할 약의 순서
결론적으로, 코드가 복잡해진다.
*/