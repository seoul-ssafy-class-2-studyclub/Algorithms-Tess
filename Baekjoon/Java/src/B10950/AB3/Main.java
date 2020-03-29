package B10950.AB3;

import java.io.*;

public class Main {
    static String[] str;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 처음에 br.readLine()으로 받을땐, String으로 들어와서 Integer.parseInt()로 타입변환을 해준다.
        int T = Integer.parseInt(br.readLine());
//        List<Integer> ans = new ArrayList<>();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));//선언
        for (int i=0; i < T; i++) {
            str = br.readLine().split(" ");
//            ans.add((Integer.parseInt(str[0])+Integer.parseInt(str[1])));
            bw.write((Integer.parseInt(str[0])+Integer.parseInt(str[1]))+"\n");//출력
        }
//        bw.flush();//남아있는 데이터를 모두 출력시킴
        bw.close();//스트림을 닫음



    }
}
