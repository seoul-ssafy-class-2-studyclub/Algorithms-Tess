class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ''
        for char in str:
            if char.isupper():
                ans += char.lower()
            else:
                ans += char
        return ans