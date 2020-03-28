package B1012.유기농배추;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    static int[] dx = { -1, 0, 1, 0 };
    static int[] dy = { 0, 1, 0, -1 };
    static int[][] arr;
    static int N;
    static int M;

    public static void main(String[] args) throws Exception {
        // BufferedReader
        // 버퍼를 이용해서 읽고 쓰는 함수
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for (int Testcase = 0; Testcase < T; Testcase++) {
            String[] str = br.readLine().split(" ");
            M = Integer.parseInt(str[0]);
            N = Integer.parseInt(str[1]);
            int K = Integer.parseInt(str[2]);
            int count = 0;
            arr = new int[N][M];
            for (int i = 0; i < K; i++) {
                str = br.readLine().split(" ");
                arr[Integer.parseInt(str[1])][Integer.parseInt(str[0])] = 1;
            }
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (arr[i][j] != 0) {
                        DFS(i, j);
                        //배추 수확
                        count++;
                    }
                }
            }

            System.out.println(count);

        }
    }

    public static void DFS(int X, int Y) {

        for (int i = 0; i < 4; i++) {
            //다음 방문지 nextX,와 nextY
            int nextX = X + dx[i];
            int nextY = Y + dy[i];

            //nextX, nextY가 범위를 벗어난다면 그냥 통과한다.
            if (nextX < 0 || nextY < 0 || nextX >= N || nextY >= M) {
                continue;
            }
            //다음 방문할 값이 0 이라면 그냥 통과한다.
            if (arr[nextX][nextY] == 0) {
                continue;
            }
            //방문한점은 0으로 바꿔준다.
            arr[nextX][nextY] = 0;
            DFS(nextX, nextY);
        }
    }
}
