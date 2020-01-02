
import collections
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = collections.deque([])
        for a in A:
            if a % 2 == 1:
                ans.append(a)
            if a % 2 == 0:
                ans.appendleft(a)
        return ans




class Solution(object): # 이게 더 느림
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left = []
        right = []
        for a in A:
            if a%2 == 1:
                right.append(a)
            if a%2 == 0:
                left.append(a)
        return left+right