package B10828.MyStack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int T;
    static List<Integer> integerList = new ArrayList<>();
    static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            // push인 경우 2 반환
            switch (st.nextToken()) {
                case "push": push(Integer.parseInt(st.nextToken())); break;
                case "pop": ans = pop(); sb.append(ans+"\n"); break;
                case "size": ans = size(); sb.append(ans+"\n"); break;
                case "empty": ans = empty(); sb.append(ans+"\n"); break;
                case "top": ans = top(); sb.append(ans+"\n"); break;
            }
        }
        System.out.println(sb);
    }

    static void push(Integer num) {
        integerList.add(num);
    }


    static int pop() {
        if (integerList.size() != 0) {
            return integerList.remove((integerList.size() - 1));
        }
        return -1;
    }

    static int size() {
        return integerList.size();
    }

    static int empty() {
        if (integerList.size() != 0) {
            return 0;
        }
        return 1;
    }

    static int top() {
        if (integerList.size() != 0) {
            return integerList.get((integerList.size()-1));
        }
        return -1;
    }
}
