class Solution(object):
    def containsDuplicate(self, nums):
        mydict = {}
        for n in nums:
            if mydict.get(n):
                return True
            if not mydict.get(n):
                mydict[n] = 1
        return False


# Runtime: 116 ms, faster than 20.24% of Python online submissions for Contains Duplicate.
# Memory Usage: 17.8 MB, less than 5.55% of Python online submissions for Contains Duplicate.


class Solution(object):
    def containsDuplicate(self, nums):
         return True if len(set(nums)) < len(nums) else False

# Runtime: 92 ms, faster than 99.75% of Python online submissions for Contains Duplicate.
# Memory Usage: 17.2 MB, less than 50.00% of Python online submissions for Contains Duplicate.

# set이 중복을 없애주는데 중복이 없어지는 경우 set전의 nums가 더 커지니까 True를 반환한다.
# for로 돌 필요가 없어져서 빨라진다.