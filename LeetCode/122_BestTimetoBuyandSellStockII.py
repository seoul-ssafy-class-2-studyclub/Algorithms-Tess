# prices = [7,1,5,3,6,4]
#
#
# def solve(st, check, profit, paid, cnt):
#     global mymax, N
#
#     # 종료조건이 너무 애매한데?
#     mymax = max(profit, mymax)
#
#     for nxt in range(st+1, N):
#         if check == 0: # 샀으면, 팔아야지
#             solve(nxt, 1, profit + (prices[nxt] - paid), 0, cnt+1)
#             # 둘다 말고 그냥 넘어가는 경우도 있어야지
#             solve(nxt, 0, profit, paid, cnt + 1)
#         if check == 1: # 전에 팔았으면, 사야지
#             solve(nxt, 0, profit, prices[nxt], cnt + 1)
#
# mymax = -1e9
# N = len(prices)
# for start in range(N):
#     solve(start, 0, 0, prices[start], 1)
#
# print(mymax)


# 시간이 너무 오래 걸린다.
# 값을 저장해나갈 수 있나?
# prices = [7,1,5,3,6,4]
# mymax = 0
# N = len(prices)
# for start in range(N):
#     stack = [(start, 0, 0, prices[start], 1)]
#     while stack:
#         st, check, profit, paid, cnt = stack.pop()
#         mymax = max(profit, mymax)
#
#         for nxt in range(st+1, N):
#             if check == 0:
#                 stack.append((nxt, 1, profit + (prices[nxt] - paid), 0, cnt+1))
#                 stack.append((nxt, 0, profit, paid, cnt + 1))
#
#             if check == 1:
#                 stack.append((nxt, 0, profit, prices[nxt], cnt + 1))
# print(mymax)

prices = [1,2,3,4]

## 애초에 dfs로 접근할 필요가 없었던 문제
mymax = 0

if len(prices) <= 1:
    print(mymax)
    # return mymax
else:
    for idx in range(1, len(prices)):
        if prices[idx] > prices[idx-1]:
            mymax += (prices[idx] - prices[idx-1])
    print(mymax)
    # return mymax


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mymax = 0
        if len(prices) <= 1:
            return mymax

        else:
            for idx in range(1, len(prices)):
                if prices[idx] > prices[idx - 1]:
                    mymax += (prices[idx] - prices[idx - 1])
            return mymax







