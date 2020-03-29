package B2577.NumsofNums;

//Counting Sort

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int myMulti;

    public static void main(String[] args) throws IOException {
        int[] ans = new int[10];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        myMulti = Integer.parseInt(br.readLine());
        for (int i = 0; i < 2; i ++){
            myMulti *= Integer.parseInt(br.readLine());
        }

        String[] arr = Integer.toString(myMulti).split("");

        int myIndex;
        for (int i = 0; i < arr.length; i++){
            myIndex = Integer.parseInt(arr[i]);
            ans[myIndex] += 1;
        }

        for (Integer num : ans) {
            System.out.println(num);
        }
    }
}
