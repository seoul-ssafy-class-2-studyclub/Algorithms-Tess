class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        '''
        On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

        Once you pay the cost, 
        you can either climb one or two steps. 
        
        You need to find minimum cost to reach the top of the floor,
        and you can either start from the step with index 0, 
        or the step with index 1.
        '''

        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
            # f1이 현재 값이 되며, f2는 그 이전의 값으로 저장된다.
            # f1 : 뒤에서 시작하는 숫자와 f1, f2의 값중에 작은 것을 더한 값
            # f2 : 더해지기 전의 이전 값
        return min(f1, f2)