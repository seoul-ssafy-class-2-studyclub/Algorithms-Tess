package kr.ac.kopo.day04.project;

import java.util.Scanner;

/**
 *
 *
 5개의 짝수를 입력받아 출력하는 코드를 작성
 1's 정수 : 12
 2's 정수 : 5
 2's 정수 : 20
 3's 정수 : 10
 4's 정수 : 26
 5's 정수 : 5
 5's 정수 : 11
 5's 정수 : 4

 < 5개의 정수 출력 >
 12   20   10   26   4
 */
public class Project02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] intArray = new int[5];
        int num = 1;
        int tempNum = 0;
        while (num != 6) {
            System.out.printf("%d's 정수 : ", num);
            tempNum = sc.nextInt();
            if ( tempNum % 2 == 0) { // 나누어 떨어지면,
                intArray[num-1] += tempNum; // 저장해준다.
                num += 1;
            }
        }
        System.out.println("< 5개의 정수 출력 >");
        for (int ans : intArray) {
            System.out.printf("%d  ", ans);
        }
    }
}
