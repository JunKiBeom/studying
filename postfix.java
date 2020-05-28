import java.util.*;

public class postfix {
    public static void main(String[] args) {
        Stack st = new Stack();
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        char e =0;
        int prec1=0, prec2=0;
        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            prec1=3;
            switch (ch) {
                case '*':
                case '/':
                case '+':
                case '-':
                    if (ch=='+' || ch=='-')
                        prec1=1;
                    else if (ch=='*' || ch=='/')
                        prec1=2;

                    if (st.isEmpty()==false) {
                        e = (char) st.peek();
                        if (e=='+' || e=='-')
                            prec2 = 1;
                        else if (e=='*' || e=='/')
                            prec2 = 2;
                        while (prec1 <= prec2) {
                            e= (char) st.pop();
                            System.out.print(e);
                            if (st.isEmpty()==false) {
                                e = (char) st.peek();
                                if (e=='+' || e=='-')
                                    prec2 = 1;
                                else if (e=='*' || e=='/')
                                    prec2 = 2;
                            }
                            else
                                break;
                        }
                    }
                    st.push(ch);
                    break;

                case '(':
                    st.push(ch);
                    break;

                case ')':
                    e = (char) st.peek();
                    while (e!='('){
                        System.out.print(e);
                        e = (char) st.pop();
                    }

                default:
                    System.out.print(ch);
                    break;
            }
        }
        do {
            e = (char) st.pop();
            System.out.print(e);
        } while (st.isEmpty()==false);
    }
}

// 2+3*4-1
// 234*+1-