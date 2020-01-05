class Solution(object):
    def findLengthOfLCIS(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        else:
            st = nums[0]
            cnt = 1
            mymax = -1e9
            for s in nums[1:]:
                if s > st:
                    st = s
                    cnt += 1
                else:
                    mymax = max(mymax, cnt)
                    st = s
                    cnt = 1
            mymax = max(mymax, cnt)
            return mymax



ans = anchor = 0
for i in range(len(nums)):
    if i and nums[i-1] >= nums[i]:
        anschor = i
    else:
        ans = max(ans, i-anchor+1)
return ans
