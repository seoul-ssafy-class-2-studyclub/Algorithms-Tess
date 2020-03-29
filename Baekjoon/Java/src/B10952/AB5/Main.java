package B10952.AB5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int A;
    static int B;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        stop: while (true){
            try {
                StringTokenizer tokenizer1 = new StringTokenizer(br.readLine());
                A = Integer.parseInt(tokenizer1.nextToken());
                B = Integer.parseInt(tokenizer1.nextToken());
                sb.append((A + B) + "\n");
            } catch (Exception e) {
                break stop;
            }
        }
        System.out.println(sb);
    }
}
