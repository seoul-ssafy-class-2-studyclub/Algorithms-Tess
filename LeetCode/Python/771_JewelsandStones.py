# 이게 제일 빠름
class Solution(object):
    def numJewelsInStones(self, J, S):
        cnt = 0
        for s in S:
            if s in J:
                cnt += 1
        return cnt
# Runtime: 12 ms, faster than 94.50% of Python online submissions for Jewels and Stones.
# Memory Usage: 11.7 MB, less than 53.76% of Python online submissions for Jewels and Stones.


class Solution(object):
    def numJewelsInStones(self, J, S):
        mydict = dict()
        for j in J:
            if mydict.get(j) == None:
                mydict[j] = 1
                continue
        mysum = 0
        for s in S:
            if mydict.get(s) != None:
                mysum += 1
        return mysum


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        for j in J:
            for s in S:
                if j == s:
                    cnt += 1
        return cnt



class Solution(object):
    def numJewelsInStones(self, J, S):
        Jset = set(J)
        return sum(s in Jset for s in S)