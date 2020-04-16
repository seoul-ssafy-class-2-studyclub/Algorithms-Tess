package kr.ac.kopo.day04.project;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 *
 *
 짝수, 홀수 따로 출력 후, 짝수sum, 홀수sum을 구하고 나중에 출력한다.
 10개의 정수를 입력받아 다음과 같이 출력하는 코드를 작성하시오.

 1's num : 12
 2's num : 5
 3's num : 8
 4's num : 30
 5's num : 22
 6's num : 87
 7's num : 9
 8's num : 4
 9's num : 15
 10's num : 22

 < 짝수 >
 12  8  30  22  4  22
 짝수의 총합 : XXX

 < 홀수 >
 5  87  9  15
 홀수의 총합 : XXX

 */
public class Project01 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 방식1
        // 참조형 배열을 사용하지 않는 방법은, 10개의 수를 모두 배열에 저장해놓고,
        // for문으로 전체 순회를 하면서 짝수와 홀수를 따로따로 출력하면 될 것 같다.
        int[] intArray = new int[10];
        int num1 = 0;
        int evenSum1 = 0;
        int oddSum1 = 0;
        for (int i = 0; i < 10; i++) {
            System.out.printf("%d's num : ", i+1);
            num1 = sc.nextInt();
            intArray[i] += num1;
        }

        System.out.println("< 짝수 >");
        for (Integer ans : intArray) {
            if (ans%2 == 0) {
                System.out.printf("%d  ", ans);
                evenSum1 += ans;
            }

        }
        System.out.println();
        System.out.printf("짝수의 총합 : %d\n", evenSum1);
        System.out.println("< 홀수 >");
        for (int ans : intArray) {
            if (ans%2 == 1) {
                System.out.printf("%d  ", ans);
                oddSum1 += ans;
            }
        }
        System.out.println();
        System.out.printf("홀수의 총합 : %d\n", oddSum1);

        // 또는,
        // 방식2
        // 짝수와 홀수가 몇개가 들어올지 모르는 경우가 있을 것 같아서
        // 참조형 배열을 사용하여 선언했다.
        ArrayList<Integer> evenArrayList = new ArrayList<>();
        ArrayList<Integer> oddArrayList = new ArrayList<>();
        int num = 0;
        int evenSum = 0;
        int oddSum = 0;

        for (int i = 1; i <= 10; i++) {
            System.out.printf("%d's num : ", i);
            num = sc.nextInt();

            if (num%2 == 0) { // 짝수의 경우
                evenArrayList.add(num);
                evenSum += num;
            } else { // 홀수의 경우
                oddArrayList.add(num);
                oddSum += num;
            }
        }

        System.out.println("< 짝수 >");
        for (Integer ans : evenArrayList) {
            System.out.printf("%d  ", ans);
        }
        System.out.println();
        System.out.printf("짝수의 총합 : %d\n", evenSum);
        System.out.println("< 홀수 >");
        for (Integer ans : oddArrayList) {
            System.out.printf("%d  ", ans);
        }
        System.out.println();
        System.out.printf("홀수의 총합 : %d\n", oddSum);


    }
}
