class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        '''
        1) target 보다 큰 값이 나오면 그 값을 리턴한다
        2) 만약 target보다 큰 값을 발견하지 못한경우 그냥 가장 작은 값을 리턴한다.
        
        '''
        for c in letters:  # c를 돌면서
            if c > target:  # target보다 크면 리턴
                return c
        return letters[0]  # 그렇지 않으면 가장 작은 값을 리턴




