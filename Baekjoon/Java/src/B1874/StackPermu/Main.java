package B1874.StackPermu;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    static Stack<Integer> stack = new Stack<>();
    static int N;
    static int Curr;
    static int i = 1;
    static int j = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine())+1;
        // stack에 1부터 추가한다.
        // 추가하면서 동시에 들어오는 애들하고 비교한다.

        StringBuilder sb = new StringBuilder();

        stop: while (true) {
            if (j < N) {
                Curr = Integer.parseInt(br.readLine());
            } else {
                break stop;
            }
            j++;

            if (stack.isEmpty()) {
                stack.add(i);
                sb.append("+\n");
                i++;
            }

            SecStop : while (true) {
                Integer last = stack.peek();
                if (!stack.isEmpty() && !last.equals(Curr)) { // 마지막꺼랑 현재꺼랑 다르다면,
                    if (i > N) { // 더 커지면 더이상 볼 필요가 없다.
                        break stop;
                    } else {
                        stack.add(i);
                        sb.append("+\n");
                        i++;
                    }
                } else if (last.equals(Curr)) { // 마지막꺼랑 현재꺼랑 같다면,
                    stack.pop();
                    sb.append("-\n");
                    break SecStop;
                }
            }
        }
        if (stack.isEmpty()) {
            System.out.println(sb);
        } else {
            System.out.println("NO");
        }
    }
}


/*
+
-
+
+
+
-
-
-
+
-
5
1
4
3
2
5
*/