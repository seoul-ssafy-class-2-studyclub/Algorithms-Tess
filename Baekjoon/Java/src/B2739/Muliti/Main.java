package B2739.Muliti;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int A;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        A = Integer.parseInt(str);

        for (int i=1; i<10; i++) {
            System.out.println(A  + " * "+ i + " = "+ (A*i));
        }
    }
}
