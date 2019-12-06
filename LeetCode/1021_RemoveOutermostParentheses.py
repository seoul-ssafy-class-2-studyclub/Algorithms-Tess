class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # delete the outermost '()'
        ans = ''
        cnt = 0
        for s in S:
            # 1. when the s is opened and cnt is zero
            # plus 1
            if s == '(' and cnt == 0:
                cnt += 1
            # 2. plus 1 when the s is opened and cnt is more than zero
            # plus 1 and add '(' to ans
            elif s == '(' and cnt > 0:
                cnt += 1
                ans += '('
            # 3. if the s is closed
            # minus 1
            # 3-1. if cnt is not zero, add ')' to ans
            elif s == ')':
                cnt -= 1
                if cnt != 0:
                    ans += ')'
        return ans