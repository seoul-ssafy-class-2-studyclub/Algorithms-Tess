 package kr.ac.kopo.day04.project;

/**
 에라토스테네스체 알고리즘
 2 ~ 100사이의 소수를 출력하는 코드를 작성

 < 2 ~ 100사이의 소수 출력 >
 2  3  5  7  11 13  17 … 97

 <교수님 설명>
 1) 2부터 100까지 숫자 저장
 2) 2를 제외하고 2의 배수를 찾아 0으로 만든다. (소수일 수 없는 애)
 3) 0으로 안바뀐애는 이 자체가 소수
 4) 3을 제외하고 3의 배수를 0으로 만든다.
 5) 숫자와 0이 아닌 숫자로 구성되는데, 그게 소수가 된다.
 */
public class Project0501 {

    public static void main(String[] args) {

        int[] intArray = new int[101]; // 편의상 101까지 늘린다.

        // 2와 3은 소수이므로 미리 저장한다.
        intArray[2] = 2;
        intArray[3] = 3;

        System.out.println("< 2 ~ 100사이의 소수 출력 >");
        System.out.printf("%d ", intArray[2]);
        System.out.printf("%d ", intArray[3]);

        // 4부터 시작한다.
        for (int i = 4; i <= 100; i++) {
            if (!(i%2 == 0) && !(i%3 ==0)) {
                intArray[i] += i; // 발견된 소수는 배열에 저장해준다.
                System.out.printf("%d ", i); // 소수를 발견하면 바로 출력해준다.
            }
        }
        // 배열에 0이 아닌 수는 모두 소수로 저장되어있다.
    }
}
