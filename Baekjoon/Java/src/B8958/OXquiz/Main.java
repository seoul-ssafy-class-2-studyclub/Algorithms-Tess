package B8958.OXquiz;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int T;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int i=0; i<T; i ++) {
            String[] st = br.readLine().split("");
            int mysum = 0;
            int myO = 0;
            for (String OX : st) {
                if (OX.equals("O")){
                        myO += 1; mysum+=myO;
                } else {
                    myO = 0;
                }
            }
            sb.append(mysum + "\n");
        }
        System.out.println(sb);
    }
}
