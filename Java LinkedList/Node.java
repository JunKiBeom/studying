//연결고리, data 구현 (Node의)
public class Node {
    private String data; //data (중요한 정보라 private 설정)
    public Node next; //다음 노드를 가리키는 고리

    Node(String input) //생성자 안에 값을 집어넣고 생성 ()안에
    {
        data = input;
    }
    public String getData()
    {
        return data;
    }
}