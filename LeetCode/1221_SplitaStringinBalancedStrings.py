'''
we only need to count the number of L and R encountered,
and add 1 to the number of splits each time these numbers are equal
when iterating through S.
'''


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        res = 0
        for index in range(len(s)):
            if s[index] == 'L':
                ans += 1
            else:
                ans -= 1
            if ans == 0:
                res += 1
        return res