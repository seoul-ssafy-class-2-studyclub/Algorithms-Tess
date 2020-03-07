class Solution(object):
    def twoSum(self, nums, target):

        first = dict()
        for i in range(len(nums)):
            first[target - nums[i]] = i

        for value, idx in first.items():
            for j in range(len(nums)):
                if value == nums[j]:
                    return [idx, j]


'''
저장해두고 해시로 값을 가져오는게 더 빠르다.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement={}
        for i in range(len(nums)):
            if nums[i] in complement:
                return [complement[nums[i]], i]
            else:
                complement[target-nums[i]]=i