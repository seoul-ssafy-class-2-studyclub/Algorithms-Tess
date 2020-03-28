package B2588.Multi;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int A;
    static int B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str1 = br.readLine(); // String으로 받아서 Int로 전환
        String str2 = br.readLine();
        String[] str3 = str2.split("");;
        A = Integer.parseInt(str1);
        int lengt = str3.length - 1;
        while (lengt != -1) {

            B = Integer.parseInt(str3[lengt]);
            System.out.println(A * B);

            lengt--;
        }
        System.out.print(A*Integer.parseInt(str2));
    }
}
