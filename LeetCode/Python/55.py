class Solution(object):
    def canJump(self, nums):
        if nums == []: return False
        mymax = nums[0]
        N = len(nums)
        if N == 1: return True
        goalIdx = N-1
        for idx in range(1, N):
            if mymax < idx:
                return False
            mymax = max(mymax, idx + nums[idx])
            if mymax >= goalIdx:
                return True
# 현재인덱스+해당인덱스의값은 다음위치의 인덱스를 갈 수 있는지 없는지를 판단하는 요소가 된다.