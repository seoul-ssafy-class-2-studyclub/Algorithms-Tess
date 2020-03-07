class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        '''
        #이 존재하면 앞에있는 것을 뺀다
        q로 접근?
        '''
        def build(S):
            ans = []
            for c in S:
                if c != '#': # '#'가 아니라면 c를 추가하고
                    ans.append(c)
                elif c == '#' and ans: # ans가 들어있는 상태이고 c가 '#'이라면 뒤에서 pop을 하고
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)