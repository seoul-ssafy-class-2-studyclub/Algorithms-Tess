class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        mydict = dict()
        i = 0
        for a in B:
            mydict[a] = i
            i += 1

        ans = []
        for b in A:
            ans.append(mydict[b])

        return ans


class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        mydict = dict()
        for i, a in enumerate(B): # 연산 최소
            mydict[a] = i

        return [mydict[b] for b in A] # append 없이 생성