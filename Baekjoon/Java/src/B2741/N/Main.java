package B2741.N;

import java.io.*;

public class Main {
    static int A;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        A = Integer.parseInt(br.readLine())+1;
        for (int i=1; i < A; i++) {
            System.out.println(A-i);
        }
    }
}
