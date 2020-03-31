package B10773.Zero;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main2 {
    static Stack<Integer> stack = new Stack<>();
    static int N;
    static int K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());
        for (int i=0; i < K; i++) {
            N = Integer.parseInt(br.readLine());
            if (N != 0) {
                stack.add(N);
            } else {
                stack.pop();
            }
        }
        int ans = stack.stream().mapToInt(Integer::intValue).sum();
        System.out.println(ans);
    }
}
