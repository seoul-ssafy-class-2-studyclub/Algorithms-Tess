package B2164.Card2;

import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    static int N;
    static Deque<Integer> deque = new ArrayDeque<>();
    static int last;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine())+ 1;
        for (int i = 1; i < N; i++) {
            deque.add(i);
        }
        stop: while (deque.size() != 1) {
            last = deque.pop();
            if (deque.size() == 1) {
              break stop;
            }
            last = deque.pop();
            deque.add(last);
        }
        System.out.println(deque.getFirst());
    }
}
