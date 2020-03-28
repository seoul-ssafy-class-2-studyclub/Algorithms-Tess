package B9498.ExamScore;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int A;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str =  br.readLine();
        A = Integer.parseInt(str);
        switch ((int) A/10) {
            case 10 :
            case 9:
                System.out.print("A");
                break;
            case 8:
                System.out.print("B");
                break;
            case 7:
                System.out.print("C");
                break;
            case 6:
                System.out.print("D");
                break;
            default:
                System.out.print("F");
        }
    }
}
