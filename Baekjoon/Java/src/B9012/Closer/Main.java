package B9012.Closer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    // 숫자가 0이 되면,
    // ( 1 ( 2 ) 1 ) 0 ( 1 ) 0 ) 1
    // ( 이되면  ++ )이되면 --

    static int T;
    static List<String> list = new ArrayList<>();
    static String[] strings;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(br.readLine());

        StringBuilder st = new StringBuilder();

        for (int i = 0; i < T; i++) {
            strings = br.readLine().split("");
            int wall = 0;
            if (strings[0].equals("(")) {
            stop: for (String str : strings) {
                switch (str) {
                    case "(" : wall += 1; break;
                    case ")" : wall -= 1; break;
                }
                // 개수는 맞지만, 괄호가 제대로 되어있지 않는 경우가 존재하므로 예외처리가 필요했다.
                // ())))((( 이런식으로,
                if (wall < 0) {
                  break stop;
                }
            }
            if (wall == 0) {
                st.append("YES"+"\n");
            } else {
                st.append("NO"+"\n");
                }
            }
            else {
                st.append("NO"+"\n");
            }
        }
        System.out.println(st);
    }
}
