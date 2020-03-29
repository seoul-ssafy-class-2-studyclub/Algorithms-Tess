package B2562.MaxValue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int myMax = 0;
    static int myMaxIndex = 0;
    static int temp = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i =1; i <10; i++ ) {
            temp = Integer.parseInt(br.readLine());
            if (myMax < temp ) {
                myMax = temp;
                myMaxIndex = i;
            }
        }

        System.out.println(myMax);
        System.out.print(myMaxIndex);
    }
}
