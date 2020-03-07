import java.util.ArrayList;
import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> complement = new HashMap<>();
        for (int i=0; i < nums.length; i++ ) {
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
