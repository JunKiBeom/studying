import java.util.Random;

public class rand {
    public static void main(String[] args) {
        Random random = new Random();
        for (int i=0;i<40;i++)
            System.out.print(random.nextInt(10));
    }
}
