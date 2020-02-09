                # if dp[idx] != 0 and idx+i <= amount:
                #     dp[idx+i] += dp[idx]
                # if idx%i == 0:
                #     print(i, dp)
                #     dp[idx] += 1


class Solution(object):
    def change(self, amount, coins):
        dp = [0]*(amount+1)
        dp[0] = 1
        for i in coins:
            for idx in range(i, amount+1):
                dp[idx] += dp[idx-i]
                # print(dp)
        return dp[amount]
