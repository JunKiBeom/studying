class scope {
    public static void main(String[] args) { // scope1
        boolean ste = true;
        int num1 = 11;
        if (ste) {                           // scope2
            // int num1 = 22;
            num1++;
            System.out.println(num1);
        }
        {                                    // scope3
            int num2 = 33;
            num2++;
            System.out.println(num2);
        }
        // System.out.println(num2); // error 발생
    }
}