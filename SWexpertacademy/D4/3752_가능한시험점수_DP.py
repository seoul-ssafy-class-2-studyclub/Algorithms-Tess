import sys
sys.stdin = open('3752.txt', 'r')

'''
#1 7
#2 11
'''

def solve(index, res): #0, 0이다.
    global result, cnt

    if index == N:
        if dp[index].get(res) == None:
            dp[index][res] = 1
            cnt += 1
        return

    elif dp[index].get(res) != None: # 만약 dp에 존재한다면 삭제
        return

    solve(index + 1, res + mylist[index]) # 선택한다.
    solve(index + 1, res) # 선택안한다.
    dp[index][res] = 1 # 과정을 저장해서 가지치기

for tc in range(int(input())):
    N = int(input())
    # dp = dict()
    dp = [{} for _ in range(N + 1)]
    mylist = list(map(int, input().split()))
    # 하나씩 재귀에 보낸다. -N 까지
    cnt = 0
    solve(0, 0)
    print(dp)
    print(f'#{tc+1}', cnt)

# for case in range(1, int(input()) + 1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     dp = {0}
#     for score in scores:
#         temp = set()
#         for num in dp: # dp에 이미 저장된 값에 더하면서 temp에 추가하고,
#             temp.add(score + num)
#         # print(temp)
#         dp.update(temp) # set을 연이어 추가하는 것이므로 update한다.
#         # print(dp)
#     print(f'#{case} {len(dp)}')

# 최적화 필요
# def solve(index, res): #0, 0이다.
#     global result
#
#     if index == N:
#         return
#
#     else:
#         solve(index + 1, res + mylist[index])
#         solve(index + 1, res)
#         res += mylist[index]
#         # if res in result:
#         #     return
#         # else:
#         result.add(res)
#
# for tc in range(int(input())):
#     N = int(input())
#
#     result = set()
#     mylist = list(map(int, input().split()))
#     # 하나씩 재귀에 보낸다. -N 까지
#     solve(0, 0)
#     print(f'#{tc+1}', len(result)+1)


'''
def bubun(res, idx):
    global cnt
​
    if idx == N:
        if maked.get(res) == None:
            cnt += 1
            maked[res] = 1
        return
​
    if cache[idx].get(res) != None:
        return
    
    bubun(res + scores[idx], idx + 1)
    bubun(res , idx + 1)
​
    cache[idx][res] = 1
    return 
​
for ro in range(int(input())):
    N = int(input())
    scores = list(map(int,input().split()))
​
    maked = dict()
    cnt = 0
    cache = [{} for _ in range(N)]
    
    bubun(0, 0)
    print('#%d %d' %(ro + 1, cnt))

'''