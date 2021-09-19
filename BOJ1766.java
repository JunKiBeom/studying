import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class BOJ1766 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();   // 문제 수
        int M = sc.nextInt();   // 정보 수
        int[] indegree = new int[N + 1];

        ArrayList<Integer>[] list = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++)
            list[i] = new ArrayList<Integer>();

        for (int i = 0; i < M; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            list[x].add(y);    //리스트 안의 리스트에 값을 넣어준다.
            indegree[y]++;    //자신을 가르키고 있는 화살표의 갯수
        }
        PriorityQueue<Integer> q = new PriorityQueue<Integer>();

        for (int i = 1; i <=N; i++) {
            if (indegree[i] == 0)
                q.add(i);
        }

        while (!q.isEmpty()) {
            int current = q.poll();
            System.out.print(current+" ");
            for (int i = 0; i < list[current].size(); i++) {
                int next = list[current].get(i);
                indegree[next]--;
                if (indegree[next] == 0) {
                    q.add(next);
                }
            }
        }
    }
}
