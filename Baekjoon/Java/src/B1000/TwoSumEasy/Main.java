package B1000.TwoSumEasy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int A;
    static int B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
//        int A;
//        int B;
        A = Integer.parseInt(str[0]);
        B = Integer.parseInt(str[1]);
        int ans = A+B;
        // 출력시 형태 확인하고 적절한 출력 메소드 사용할 것
        System.out.print(ans);
//        System.out.println(ans);
    }

}
