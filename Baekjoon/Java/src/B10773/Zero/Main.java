package B10773.Zero;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static List<Integer> list = new ArrayList<>();
    static int N;
    static int K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());
        for (int i=0; i < K; i++) {
            N = Integer.parseInt(br.readLine());
            if (N != 0) {
                list.add(N);
            } else {

                list.remove((list.size()-1));
            }
        }
        int ans = list.stream().mapToInt(Integer::intValue).sum();
        System.out.println(ans);
    }
}
