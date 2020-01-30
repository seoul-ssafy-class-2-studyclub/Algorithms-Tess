class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

    # [4,1,2,1,2]
    #
    # 4 1 2 => 7 * 2 = 14
    # - 10
    # 4

    # 2∗(a+b+c)−(a+a+b+b+c)=c
    # (a+a+b+b+c+c)-(a+a+b+b+c) => c