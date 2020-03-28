package B8393.Sum;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int A;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        A = Integer.parseInt(str);

        int ans = 0;
        for (int i = 0; i <= A; i++ ) {
            ans += i;
        }
        System.out.print(ans);
    }
}
