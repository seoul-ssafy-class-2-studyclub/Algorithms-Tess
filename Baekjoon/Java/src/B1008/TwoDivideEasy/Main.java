package B1008.TwoDivideEasy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int B;
    static int A;
    static int C;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");

        A = Integer.parseInt(str[0]);
        B = Integer.parseInt(str[1]);
        C = Integer.parseInt(str[2]);
//        System.out.println(A+B);
//        System.out.println(A-B);
//        System.out.println(A*B);
//        System.out.println(A/B);
//        System.out.println(A%B);
        System.out.println((A+B)%C);
        System.out.println(((A%C) + (B%C))%C);
        System.out.println((A*B)%C);
        System.out.println( ((A%C) * (B%C))%C);
    }
}
