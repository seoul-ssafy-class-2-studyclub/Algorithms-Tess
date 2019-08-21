import sys
sys.stdin = open('2559.txt', 'r')

N, K = map(int, input().split())
mat = list(map(int, input().split()))

# if K == 1:
#     print(max(mat))
# else:
temp = 0
for n in range(N):
    if temp < sum(mat[n:K+n]):
        temp = sum(mat[n:K+n])
print(temp)




# 1부터 자기자리의 전체 합을 누적저장하는 배열 선언 후 저장.
# 구간최대값이 나올때마다 갱신.
# 각 구간값을 한자리 더할때마다 앞자리꺼 뺀다.



# if (N//K)%2 == 1:
#     T = (N // K) + 1
# else:
#     T = N // K
# for n in range(T+4):
#     cnt = 0
#     for i in range(K):
#         cnt += mat[n+i]
#     cnt_list.append(cnt)
# res = max(cnt_list)
# print(res)