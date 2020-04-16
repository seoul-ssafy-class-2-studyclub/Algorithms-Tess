package kr.ac.kopo.day04.project;

public class Project0502 {
    public static void main(String[] args) {
        int[] intArray = new int[99]; // 편의상 101까지 늘린다.

        System.out.println("< 2 ~ 100사이의 소수 출력 >");

        for (int i = 0; i < intArray.length; i++) {
            intArray[i] = i+2;
        }

        for (int i = 0; i < intArray.length; i++) {
            // 돌면서 0이 아니라면, 소수라는 의미
            // 저장된 2부터 차례대로 돌면서 구한다.
            if (intArray[i] != 0) {
                for (int j = i+1; j < intArray.length; j ++) {
                    if(intArray[j] % intArray[i] == 0) {
                        intArray[j] = 0;
                    }
                }
            }
        }

        for (int ans : intArray) {
            if (ans != 0) {
                System.out.print(ans+" ");
            }
        }
    }
}
