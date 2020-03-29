package B1110.PlusCycle;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    // 숫자를 스트링으로 다 쪼개어 받는다.
    // 주어진 문제에서 입력인 N은 0 <= N <= 99 라고하는데,
    // 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int initNum = Integer.parseInt(st.nextToken());
        int num = initNum;
        System.out.println(initNum);
        System.out.println(num);
        int cnt = 0;
        while (initNum != num || cnt == 0) {
            num = (num%10)%10 + (num/10+num%10)%10;
            cnt++;
        }
        System.out.println(cnt);
    }
}
