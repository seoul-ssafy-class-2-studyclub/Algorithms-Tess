package B18258.Queue2;

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int pushword;
    static Queue<Integer> stringList = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            switch (st.nextToken()) {
                case ("push") : push(Integer.parseInt(st.nextToken())); break;
                case ("pop") : sb.append(pop()+"\n"); break;
                case ("size") : sb.append(size1()+"\n"); break;
                case ("empty") : sb.append(empty()+"\n"); break;
                case ("front") : sb.append(front()+"\n"); break;
                case ("back") : sb.append(back()+"\n"); break;
            }
        }
        bw.write(String.valueOf(sb));
        bw.flush();
        bw.close();

    }

    static void push(Integer num) {
        stringList.offer(num);
        pushword = num;
    }

    static int pop() {
        if (stringList.isEmpty()) {
            return -1;
        } else {
            return stringList.poll();
        }
    }

    static int size1() {
        return stringList.size();
    }

    static int empty() {
        if (stringList.isEmpty()) {
            return 1;
        } else {
            return 0;
        }
    }

    static int front() {
        if (stringList.isEmpty()) {
            return -1;
        } else {
            return stringList.peek();
        }
    }

    static int back() {
        if (stringList.isEmpty()) {
            return -1;
        } else {
            return pushword;
        }
    }
}
