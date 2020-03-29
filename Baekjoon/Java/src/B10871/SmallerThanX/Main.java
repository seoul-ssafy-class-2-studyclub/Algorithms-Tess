package B10871.SmallerThanX;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class Main {
    // Stream으로 풀어보자
    static int N;
    static int X;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer1 = new StringTokenizer(br.readLine());
        N = Integer.parseInt(tokenizer1.nextToken());
        X = Integer.parseInt(tokenizer1.nextToken());

        String[] str = br.readLine().split(" ");

        int[] array = Arrays.stream(StringArrayToIntArray(str))
                .filter(x -> x < X )
                .toArray();

        StringBuilder sb = new StringBuilder();
        for(int num : array) { sb.append(num).append(" "); }
        System.out.println(sb);
    }
    static int[] StringArrayToIntArray(String[] stringArray)
    {
        return Stream.of(stringArray).mapToInt(Integer::parseInt).toArray();
    }
}


/*

int[] list = Arrays.stream(new Integer[] {1,2,3,4,5,6})
        .filter(x -> x > 3)
        .collect(toList());
Or keep working with an IntStream, and box it to a Stream<Integer> later in order to collect the elements to a List<Integer>:

int[] list = Arrays.stream(new int[] {1,2,3,4,5,6})
                 .filter(x -> x > 3)
                 .boxed()
                 .collect(toList());
If you wish to to keep working with ints, you can produce an int array from the elements of the filtered IntStream:

int[] array = Arrays.stream(new int[] {1,2,3,4,5,6})
                  .filter(x -> x > 3)
                  .toArray();
 */