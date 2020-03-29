package B11021.AB7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int T;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine())+1;
        int A;
        int B;
        for (int i = 1; i < T; i++) {
            String[] str = br.readLine().split(" ");
            A = Integer.parseInt(str[0]);
            B = Integer.parseInt(str[1]);
            System.out.println("Case #"+i+": "+ A+" + "+B+" = "+(A+B));
        }
    }
}
