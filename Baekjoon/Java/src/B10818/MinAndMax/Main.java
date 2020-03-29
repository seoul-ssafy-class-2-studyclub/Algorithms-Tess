package B10818.MinAndMax;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class Main {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        String[] str = br.readLine().split(" ");

        int max = Arrays.stream(Stream.of(str).mapToInt(Integer::parseInt).toArray()).max().getAsInt();
        int min = Arrays.stream(Stream.of(str).mapToInt(Integer::parseInt).toArray()).min().getAsInt();
        sb.append(min).append(" ").append(max);
        System.out.println(sb);
    }
}
// Stream으로 min/max 가져오기
// Stream으로 하긴했는데 뭔가 더 비효율적인거 같다.
// 어떻게 해야 한 스트림 안에서 min이랑 Max 둘다 가져올 수 있을까?
// 답은, 그렇게 할 수 없다인 듯.. 아무래도 stream에서 .min() .max()를 한 번에 사용하면 로직이 이상해지기 때문이다.
// 그냥 이런문제는 stream을 사용하지 않는게 훨씬 빠른 것 같다.
// 그냥 풀었다면,
// place sorting으로 풀어야 한다면,
// 3개의 포인터를 사용하는데,
// 가장 작은 걸 앞으로 가면서 기준점을 잡고, 가장 작은것보다 큰걸 살려가면서 포인터를 옮겨가는 식으로 최소 최대를 구할 것 같다.
