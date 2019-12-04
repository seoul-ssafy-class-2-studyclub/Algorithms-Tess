'''
simple problem
used the for loop for iterating over the list of the str elements
I used the fin as a point to differ '[.' or ']' when it comes to '.'
'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        # print(address)
        ans = ''
        fin = 0
        for char in address:
            if char == '.':
                if fin == 0:
                    ans += '[.'
                    fin = 1
                if fin == 1:
                    ans += ']'
                    fin = 0
            if char != '.':
                ans += char
        return ans