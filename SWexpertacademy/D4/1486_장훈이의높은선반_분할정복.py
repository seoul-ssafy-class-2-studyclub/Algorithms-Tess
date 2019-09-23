import sys
sys.stdin = open('1486.txt', 'r')
'''
#1 1
#2 4
#3 27
#4 11
#5 42
#6 32
#7 2
#8 3
#9 25
#10 0
'''

def perm(now, total):
    global res
    if total >= B: # 순서 ! 실수, B를 넘어서는 순간 바로 리턴해주면 된다.
        if res > total - B:
            res = total - B
    if now >= N:
        return True
    perm(now+1, total + mylist[now]) # 현재를 넣고, 인덱스도 증가
    perm(now+1, total) # 현재를 안넣고, 인덱스만 증가

for tc in range(int(input())):
    N, B = map(int, input().split())
    mylist = list(map(int, input().split()))
    res = float('inf')
    perm(0, 0)
    print(f'#{tc+1}', res)


#
# def top(K, score):
#     global result
#     if score >= B:
#         if result > score - B:
#             result = score - B
#     if K >= N:
#         return
#     top(K + 1, score + men[K])
#     top(K + 1, score)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, B = map(int, input().split())
#     men = list(map(int, input().split()))
#     result = 999999
#     men.sort(reverse=True)
#     top(0, 0)
#     print('#{} {}'.format(tc, result))
#





#
# for test in range(int(input())):
#     n, b = map(int, input().split())
#     heights = list(map(int, input().split()))
#     differs = []
#     for i in range(1 << n):
#         total = 0
#         for j in range(n + 1):
#             if i & (1 << j):
#                 total += heights[j]
#                 if total >= b:
#                     differs.append(total - b)
#                     break
#
#     print('#{} {}'.format(test + 1, min(differs)))


'''
for test in range(int(input())):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    differs = []
    for i in range(1 << n):
        total = 0
        for j in range(n+1):
            if i & (1 << j):
                total += heights[j]
                if total >= b:
                    differs.append(total-b)
                    break
 
    print('#{} {}'.format(test+1, min(differs)))

'''