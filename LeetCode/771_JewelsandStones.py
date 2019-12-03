## Leetcode Start!
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        for j in J:
            for s in S:
                if j == s:
                    cnt += 1
        return cnt