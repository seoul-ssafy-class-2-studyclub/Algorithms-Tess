import java.util.ArrayList;
import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> complement = new HashMap<>();
        for (int i=0; i < nums.length; i++ ) {
            System.out.println(complement);
//            System.out.println();
            System.out.println(complement.containsKey(nums[i]));
            if (complement.containsKey(nums[i]) == false) {
                System.out.println(nums[i]);
                complement.put(target-nums[i], i);
            } else { // true 라면,
                int[] ans = new int[2];
                System.out.println(ans.toString());
                ans[0] = complement.get(nums[i]);
                ans[1] = i;
                System.out.println(ans);
                return ans;
            }
        }
        // 자바는 꼭 리턴값이 있어야 한다.
        return null;
    }
}
