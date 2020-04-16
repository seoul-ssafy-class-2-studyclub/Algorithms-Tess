package kr.ac.kopo.day04.project;

import java.util.Scanner;

/**
 다음의 결과를 보이는 프로그램을 작성하시오.
 int[] nums = new int[30];

 1 – 100사이의 정수를 입력하시오 : 64
 64의 약수의 개수 : 7개
 < 64의 7개 약수 출력 >
 1 2 4 8 16 32 64

 1 – 100사이의 정수를 입력하시오 : 79
 79의 약수의 개수 : 2개

 < 79의 2개 약수 출력 >
 1 79

 약수는 어떤 수로 정수가 나누어떨어지는것을 말한다.

 */
public class Project04 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = new int[30];
        System.out.print("1 – 100사이의 정수를 입력하시오 : ");
        int num = sc.nextInt();
        int count = 0;
        for (int i=1; i <= num; i++) {
            if (num%i==0) { // 0이면, 약수이므로 저장해준다.
                nums[count] = i;
                count++;
            }
        }
        System.out.printf("< %d의 %d개 약수 출력 > \n", num, count);

        for (int i=0; i < count; i++) { // 하나씩 출력해준다.
            System.out.printf("%d ", nums[i]);
        }
    }
}
