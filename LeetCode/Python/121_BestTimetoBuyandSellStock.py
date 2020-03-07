class Solution(object):
    def maxProfit(self, prices):
        length = len(prices)
        if length == 0: return 0
        minNumber = prices[0] # 가장 작은 값을 계속 가지고 있으면 된다.
        profit = 0 # 그리고 그 값보다 큰게 나왔을때의 이익을 구해주면서 한 번 돌아주면 끝
        for idx in range(1, length): # O(N)
            if minNumber > prices[idx]:
                minNumber = prices[idx]
            else:
                if profit < prices[idx] - minNumber:
                    profit = prices[idx] - minNumber
        return profit
# Runtime: 44 ms, faster than 89.31% of Python online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 12.6 MB, less than 39.45% of Python online submissions for Best Time to Buy and Sell Stock.