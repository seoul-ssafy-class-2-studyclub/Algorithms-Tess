package B4949.CoserWorld;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    static String[] strings;
    static Stack<String> stack = new Stack<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        stop: while (true) {
            strings = br.readLine().split("");
            if (strings[0].equals(".") && strings.length == 1) {
                break stop;
            } else {
                stopSec: for (String st : strings) {
                    if (st.equals("(") || st.equals("[")) {
                        stack.add(st);
                    } else if (st.equals(")") || st.equals("]")) {
                        if (stack.isEmpty()) {
                            stack.add("dummy");
                            break stopSec;
                        }
                        if (!stack.isEmpty()) {
                            String last = stack.peek();
                            if (last.equals("(") && st.equals(")")) {
                                stack.pop();
                            } else if (last.equals("[") && st.equals("]")) {
                                stack.pop();
                            } // [)))] 이 경우, 그냥 틀린거임
                            else if (last.equals("[") && !st.equals("]")) {
                                stack.add("dummy");
                                break stopSec;
                            }
                            else if (last.equals("(") && !st.equals(")")) {
                                stack.add("dummy");
                                break stopSec;
                            }
                        }
                    }
                }
            }
            if (stack.isEmpty()) {
                sb.append("yes\n");
                stack.clear();
            } else {
                sb.append("no\n");
                stack.clear();
            }
        }
        System.out.println(sb);
    }
}
