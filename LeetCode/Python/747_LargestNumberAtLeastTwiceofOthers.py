class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums안에 가장 큰 값이 있고, 중복되지 않는다.
        # 리스트안에서 가장 큰 값을 찾는데, 그 외의 원소들보다 적어도 2배 더 큰 원소여야 한다.
        # 만약 그렇다면 index를 출력하고, 그런 경우가 아니라면 -1을 출력

        '''
        전체를 돌면서 가장 큰 값을 찾는다.
        큰 값의 인덱스를 저장한다.
        가장 큰 값을 제외한 다른 값들 모두가 
        큰값/2를 한 값의 이하인 경우 큰 값의 인덱스를 리턴하고 
        그렇지 않은 경우 -1을 리턴하면 된다.
        '''

        mynums = dict()
        mymax = -1e9
        for i in range(len(nums)):
            mynums[nums[i]] = i
            if mymax < nums[i]:
                mymax = nums[i]

        partition = mymax // 2

        for i in range(len(nums)):
            if mynums[mymax] != i:
                if partition < nums[i]:
                    return -1
        return mynums[mymax]

# Runtime: 20 ms, faster than 84.15% of Python online submissions for Largest Number At Least Twice of Others.
# Memory Usage: 11.9 MB, less than 22.22% of Python online submissions for Largest Number At Least Twice of Others.

'''python library 최대한 활용 = max사용시 느려진다.'''


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums안에 가장 큰 값이 있고, 중복되지 않는다.
        # 리스트안에서 가장 큰 값을 찾는데, 그 외의 원소들보다 적어도 2배 더 큰 원소여야 한다.
        # 만약 그렇다면 index를 출력하고, 그런 경우가 아니라면 -1을 출력

        '''
        전체를 돌면서 가장 큰 값을 찾는다.
        큰 값의 인덱스를 저장한다.
        가장 큰 값을 제외한 다른 값들 모두가 
        큰값//2를 한 값의 이하인 경우 큰 값의 인덱스를 리턴하고 
        그렇지 않은 경우 -1을 리턴하면 된다.
        '''

        mymax = max(nums)
        partition = mymax // 2
        idx = 0

        for i in range(len(nums)):
            if nums[i] != mymax:
                if partition < nums[i]:
                    return -1
            else:
                idx = i

        return idx
# Runtime: 28 ms, faster than 26.59% of Python online submissions for Largest Number At Least Twice of Others.
# Memory Usage: 11.8 MB, less than 33.33% of Python online submissions for Largest Number At Least Twice of Others.