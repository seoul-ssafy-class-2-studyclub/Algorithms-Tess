import sys
sys.stdin = open('14501.txt', 'r')

N = int(input())

# 자료 저장
data_Name = [0]+[0]*N
data_Ti = [0]+[0]*N
data_Pi = [0]+[0]*N


for i in range(1, N+1):
    Ti, Pi = map(int, input().split())
    data_Name[i] += i
    data_Ti[i] += Ti
    data_Pi[i] += Pi
    # if N+1 < Ti+i:
    #     Capable_Candidate[i] = False # 죽은 후보 -> 여기서 죽이지 말고 나중에 통으로 죽이자.
    # print(data_Name)
    # print(data_Ti)
    # print(data_Pi)

    final_Candidate = []
    for i in range(1<<N+1):
        su_data_Name = []
        for j in range(1, N+1):
            if i&(1<<j):
                su_data_Name.append(data_Name[j])
        if su_data_Name not in final_Candidate:
            final_Candidate.append(su_data_Name) # 중복제거

    final_Candidate = [False] + final_Candidate
    numofCandidate = len(final_Candidate)
    Capable_Candidate = [False]+[True]*numofCandidate
    # print(final_Candidate)
    for idx in range(len(final_Candidate)):
        # print(final_Candidate[idx])
        cnt = 0
        if final_Candidate[idx] == False or []:
            continue
        else:
            for one in final_Candidate[idx]:
                print(one)
                print(data_Ti[one])
                cnt += data_Ti[one]
                print(cnt)
                if N+1 < cnt:
                    Capable_Candidate[idx] = False
    print(Capable_Candidate)

    real_final_Candidate = []

    for idx in range(len(Capable_Candidate)):
        if Capable_Candidate[idx] == True:
            print(final_Candidate[idx])
            real_final_Candidate.append(final_Candidate[idx])
    print(real_final_Candidate)



    #
    #     if temp != False and N+1 < data_Ti[temp_one]:
    #         Capable_Candidate = False
    # print(Capable_Candidate)


    #
    #
    #
    #
    #
    #
    #
    #
    # for temp in final_list:
    #     if len(temp) == N:
    #         if sum(temp) == K:
    #             count += 1
    # print(f'#{tc} {count}')


'''
def solve(k):
    global ans
    if k == N:
        for i in range(N):
            if Si[i]:
                for j in range(i + 1, i + Ti[i]):
                    if j >= N or Si[j] : return

        tsum = 0
        for i in range(N):
            if Si[i]:
                tsum += Pi[i]
        if tsum > ans : ans = tsum

    else:
        Si[k] = 1
        solve(k + 1)
        Si[k] = 0
        solve(k + 1)

N = int(input())

Ti = [0] * N
Pi = [0] * N
Si = [0] * N

for i in range(N):
    Ti[i], Pi[i] = map(int, input().split())

ans = 0
solve(0)

print(ans)







# def solve(k, s):
#     global ans
#     if k == N:
#         ans = max(ans, s)
#         return
#
#     if(k + Ti[k] <= N):
#         solve(k + Ti[k], s + Pi[k])
#
#     solve(k + 1, s)
#
# N = int(input())
#
# Ti = [0] * N
# Pi = [0] * N
#
# for i in range(N):
#     Ti[i], Pi[i] = map(int, input().split())
#
# ans = 0
# solve(0, 0)
#
# print(ans)


'''