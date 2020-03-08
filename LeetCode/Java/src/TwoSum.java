import java.util.ArrayList;
import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> complement = new HashMap<>();
        for (int i=0; i < nums.length; i++ ) {
            // complement에서 containsKey로 해당 키가 있는지 확인
            // python 에서 in으로 찾아보는 것과 동일
            // 혹은 .get() 과도 동일하다
            // boolean 값을 리턴해서 알려준다.
            if (complement.containsKey(nums[i]) == false) {
                complement.put(target-nums[i], i);
            } else { // true 라면,
                return new int[] {complement.get(nums[i]), i};
            }
        }
        // 자바는 꼭 리턴값이 있어야 한다.
        return null;
    }
}
