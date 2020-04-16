package kr.ac.kopo.day04.project;

import java.util.Scanner;

/**
 *
 다음의 결과를 보이는 코드를 작성하시오
 1번째 정수 : 10
 2번째 정수 : 5
 10보다 큰수가 와야합니다
 2번째 정수 : 12
 3번째 정수 : 36
 4번째 정수 : 6
 10, 12, 36보다 큰수가 와야합니다
 4번째 정수 : 22
 10, 12, 36보다 큰수가 와야합니다
 4번째 정수 : 40
 5번째 정수 : 67

 < PRINT >
 10  12  36  40  67
 < REVERSE >
 76  4  63  21  1

 */
public class Project03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // 입력객체 생성
        int[] reverseArray = new int[10];
        int[] intArray = new int[5];
        int num = 1;
        int tempNum = 0; // 초기값을 선언해주면 안전하다고 오늘 배웠다!
        int currMax = -1;
        int reverseNum = 0;
        int[] rev1 = new int[5];
        int[] rev2 = new int[5];
        while (num != 6) { // 큰수가 5개 채워질때까지 입력을 받을 것

            System.out.printf("%d번째 정수 : ", num);
            tempNum = sc.nextInt();

            if ( currMax < tempNum) {
                currMax = tempNum; // 큰수가 나올때마다 바꿔준다.
                intArray[num-1] += tempNum; // 큰수를 배열에 저장해주고,
                rev1[num-1]= tempNum/10;
                rev2[num-1]= tempNum%10;

                num += 1; // 카운트를 늘려준다.
            } else { // 저장된 큰수보다 큰수가 입력되지 않은 경우,
                for (int i =0; i < (num-1); i ++) {
                    System.out.printf("%d ", intArray[i]); // 경고를 해준다.
                }
                System.out.println("보다 큰수가 와야합니다");
            }
        }
        System.out.println();
        System.out.println("< PRINT >");
        for (int ans : intArray) {
            System.out.printf("%d  ", ans);
        }
        System.out.println(); // 예제와 동일하게 개행을 넣어준다.
        System.out.println();
        System.out.println("< REVERSE >");
        for (int i=4; i >= 0; i --) { // 뒤로가면서 출력해준다.
            if (rev2[i] != 0) {
                System.out.printf("%d", rev2[i]);
            }
            System.out.printf("%d  ", rev1[i]);

        }
    }
}
