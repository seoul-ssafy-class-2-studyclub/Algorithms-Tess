class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        N = len(nums)
        ans = [0]*N
        for i in range(N):
            for j in range(i+1, N):
                if nums[i] > nums[j]:
                    ans[i] += 1
                elif nums[j] > nums[i]:
                    ans[j] += 1
        return ans