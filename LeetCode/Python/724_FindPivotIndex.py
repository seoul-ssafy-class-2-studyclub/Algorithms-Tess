class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        total = sum(nums)
        subSum = 0
        for i in range(length):
            # 곱하기 2한 값과 현재 값을 더한게 total과 같아지면 그게 pivot이 되므로
            if ((subSum * 2 + nums[i]) == total): return i
            subSum += nums[i]
        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        length = len(nums)
        total = sum(nums)
        left = 0
        for i in range(length):
            right = total - left - nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1
