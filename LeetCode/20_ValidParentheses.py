class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["} # 먼저 저장
        for char in s: # 하나씩 돌면서,

            if char in mapping: # char이라는 ')' '}' ']' 닫는 키가 존재하면, 여는 값을 만났어야 한다. 그래서 아래와 같이 확인
                top_element = stack.pop() if stack else '#'
                # 1. stack이 있다면 여는 값을 갖고 있는거고, 그렇지 않은 경우 여는 값 없이 닫는 값만 나온 것
                if mapping[char] != top_element: # ')'은 '(' 을 값으로 가지고, 가장 먼저 들어간 여는 값과 비교된다.
                    return False
            else:
                stack.append(char)
        return not stack

# class Solution(object):
#     def isValid(self, s):
#         while "()" in s or "{}" in s or '[]' in s:
#             s = s.replace("()", "").replace('{}', "").replace('[]', "")
#         return s == ''