import java.util.Arrays;
import java.util.Scanner;

class Calculator {

    void reverse(String st, int[] arr) {
        for (int i=st.length()-1;i>=0;i--) {          // 배열 뒤집기
            if (st.charAt(i)=='-')
                continue;
            arr[st.length() - 1 - i] = st.charAt(i) - '0'; // 한글자씩 처리
        }
    }

    void plus(int[] x, int[] y, int[] r) {

        int loop = x.length>y.length ? y.length : x.length;     // 연산 횟수
        int cpy = x.length>y.length ? x.length : y.length;      // 복사 횟수
        boolean check = x.length > y.length;
        int temp = 0;
        int carry = 0;
        int cnt = 0;
        int L = 0;

        for (L=0;L<loop;L++) {
            temp=x[L]+y[L]+carry;
            carry = 0;
            r[L]=temp%10;
            carry=temp/10;
        }
        for (L=loop;L<cpy;L++){
            if (check)
                r[L]=x[L]+carry;
            else
                r[L]=y[L]+carry;
            carry = 0;
        }
        if (loop==L && carry==1) {
            r[L] = carry;
            carry = 0;
        }

        for (int i=0;r[i]!=-1;i++)
            cnt++;
        for (int i=cnt-1;i>=0;i--)                              // 거꾸로 출력
            System.out.print(r[i]);
        System.out.println();
    }

    void minus(int[] x, int[] y, int[] r) {

        int loop = x.length>y.length ? y.length : x.length;     // 연산 횟수
        int cpy = x.length>y.length ? x.length : y.length;      // 복사 횟수
        boolean check = x.length > y.length;
        int temp = 0;
        int carry = 0;
        int cnt = 0;
        int L = 0;

        for (L=0;L<loop;L++) {
            if (x[L]-y[L]+carry>=0) {
                temp = x[L] - y[L] + carry;
                carry = 0;
            }
            else {
                temp = x[L] - y[L] + carry + 10;
                carry = -1;
            }
            r[L]=temp%10;
        }
        for (L=loop;L<cpy;L++){
            if (check) {
                if (x[L] + carry >= 0) {
                    temp = x[L] + carry;
                    carry = 0;
                }
                else {
                    temp = x[L] + carry + 10;
                    carry = -1;
                }
                r[L] = temp % 10;
            }
            else {
                if (y[L] + carry >= 0) {
                    temp = y[L] + carry;
                    carry = 0;
                } else {
                    temp = y[L] + carry + 10;
                    carry = -1;
                }
                r[L] = temp % 10;

            }
//        if (cpy==L && carry==-1) {
//            r[L] = -1;
//            carry = 0;
        }

        for (int i=0;i<45;i++)
            if (r[i+1]==0&&r[i+2]==-1)
                r[i+1]=-1;

        if(Arrays.equals(x,y)) {                                // X==Y
            Arrays.fill(r,-1);
            r[0]=0;
        }

        for (int i=0;r[i]!=-1;i++)
            cnt++;
        for (int i=cnt-1;i>=0;i--)                              // 거꾸로 출력
            System.out.print(r[i]);
        System.out.println();
    }

    void multiply(int[] x, int[] y, int[] r) {

        System.out.println();
    }

    boolean check_zero(int[] arr) {
        return arr.length == 1 && arr[0] == 0;
    }

}

public class Calc {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Input X. ");
        String x = sc.next();
        System.out.print("Input Y. ");
        String y = sc.next();
        System.out.println();

        int[] arr_x, arr_y;
        boolean check_x = false, check_y = false;  // x,y가 음수 인지 아닌지 저장 <0이면 T, >0이면 F

        if (x.charAt(0)=='-') {             // 음수일 경우 -부호 제외 한 만큼만 배열 생성
            arr_x = new int[x.length() - 1];
            check_x = true;                 // X<0
        }
        else {
            arr_x = new int[x.length()];
        }
        if (y.charAt(0)=='-') {
            arr_y = new int[y.length() - 1];
            check_y = true;                 // Y<0
        }
        else {
            arr_y = new int[y.length()];
        }
        int[] result_p = new int[100];
        int[] result_s = new int[100];
        int[] result_m = new int[100];

        Arrays.fill(result_p, -1);      // -1로 전부 채우기, 배열 출력을 위한 작업
        Arrays.fill(result_s, -1);
        Arrays.fill(result_m, -1);

        Calculator cal = new Calculator();

        cal.reverse(x,arr_x);               // 배열에 문자열 뒤집으며 넣기
        cal.reverse(y,arr_y);

        // x,y 대소 비교
        int cnt_x = 0, cnt_y = 0;
        boolean big_x = false, big_y = false;
        if (arr_x.length == arr_y.length){
            for (int i=arr_x.length-1;i>=0;i--){
                if (arr_x[i]>arr_y[i])
                    cnt_x++;
                else if((arr_x[i]<arr_y[i]))
                    cnt_y++;
            }
            if(cnt_x>cnt_y)
                big_x=true;                     // |x|>|y|
            else if (cnt_x<cnt_y)
                big_y=true;                     // |x|<|y|

            if (arr_x[arr_x.length-1]>arr_y[arr_y.length-1]) {
                big_x = true; big_y = false;}
            else if (arr_x[arr_x.length-1]<arr_y[arr_y.length-1]) {
                big_x = false; big_y = true;}
        }
        else if (arr_x.length > arr_y.length)   // |x|>|y|
            big_x=true;

        else if (arr_x.length < arr_y.length)   // |x|<|y|
            big_y=true;
        //

        if ((check_x==true) && (check_y==false)) {                // X<0, Y>0

            System.out.print("X + Y = ");
            if (big_x) {                                          // |X|>|Y|
                System.out.print('-');
                cal.minus(arr_x, arr_y, result_p);                // -(|X|-Y)
                // print result
            }
            else if(big_y || ((big_x==false) && (big_y==false))) {  // |X|<|Y| || |X|==|Y|
                cal.minus(arr_y, arr_x, result_p);                // Y-X
                // print result
            }

            System.out.print("X - Y = ");
            if (big_x) {                                          // |X|>|Y|
                System.out.print('-');
                cal.plus(arr_x, arr_y, result_s);                 // -(X+Y)
                // print result
            }
            else if(big_y || ((big_x==false) && (big_y==false))) {  // |X|<|Y| || |X|==|Y|
                System.out.print('-');
                cal.plus(arr_x, arr_y, result_s);                 // -(|X|+Y)

                // print result
            }

            if (cal.check_zero(arr_x) || cal.check_zero(arr_y))
                System.out.print("X * Y = 0");
            else {
                System.out.print("X * Y = ");
                System.out.print('-');
                cal.multiply(arr_x, arr_y, result_m);             // -(X*Y)
                // print result
            }
        }

        else if ((check_x==false) && (check_y==true)) {           // X>0, Y<0

            System.out.print("X + Y = ");
            if (big_x || ((big_x==false) && (big_y==false))) {    // |X|>|Y| || |X|==|Y|
                cal.minus(arr_x, arr_y, result_p);                // X-Y
                // print result
            }
            else if(big_y) {
                System.out.print('-');// |X|<|Y|
                cal.minus(arr_y, arr_x, result_p);                // -(Y-X)
                // print result
            }

            System.out.print("X - Y = ");
            cal.plus(arr_x, arr_y, result_s);                     // X+Y

            if (cal.check_zero(arr_x) || cal.check_zero(arr_y))
                System.out.print("X * Y = 0");
            else {
                System.out.print("X * Y = ");
                System.out.print('-');
                cal.multiply(arr_x, arr_y, result_m);             // -(X*Y)
                // print result
            }
        }

        else if ((check_x==false) && (check_y==false)) {          // X>0, X>0

            System.out.print("X + Y = ");
            cal.plus(arr_x, arr_y, result_p);                     // X+Y
                // print result

            System.out.print("X - Y = ");
            if (big_x || ((big_x==false) && (big_y==false))) {    // |X|>|Y| || |X|==|Y|
                cal.minus(arr_x, arr_y, result_s);                // X-Y
                // print result
            }
            else if(big_y) {
                System.out.print('-');// |X|<|Y|
                cal.minus(arr_y, arr_x, result_s);                // -(Y-X)
                // print result
            }

            if (cal.check_zero(arr_x) || cal.check_zero(arr_y))
                System.out.print("X * Y = 0");
            else {
                System.out.print("X * Y = ");
                cal.multiply(arr_x, arr_y, result_m);             // X*Y
                // print result
            }
        }

        else if ((check_x==true) && (check_y==true)) {            // X<0, Y<0

            System.out.print("X + Y = ");
            System.out.print('-');
            cal.plus(arr_x, arr_y, result_p);                     // -(X+Y)
            // print result

            System.out.print("X - Y = ");
            if (big_x) {                                          // |X|>|Y|
                System.out.print('-');
                cal.minus(arr_x, arr_y, result_s);                // -(X-Y)
                // print result
            }
            else if(big_y || ((big_x==false) && (big_y==false))) {  // |X|<|Y| || |X|==|Y|
                cal.minus(arr_y, arr_x, result_s);                // (Y-X)
                // print result
            }

            if (cal.check_zero(arr_x) || cal.check_zero(arr_y))
                System.out.print("X * Y = 0");
            else {
                System.out.print("X * Y = ");
                cal.multiply(arr_x, arr_y, result_m);             // X*Y
                // print result
            }
        }


    }
}