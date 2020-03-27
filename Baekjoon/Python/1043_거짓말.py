import sys
sys.stdin = open('1043.txt', 'r')

'''
입력
사람의 수 N이 주어진다. 
그리고 그 이야기의 진실을 아는 사람이 주어진다. 
그리고 각 파티에 오는 사람들의 번호가 주어진다. 

출력
과장된 이야기를 할 수 있는 파티 개수의 최댓값
'''


# index때문에 runtime error 났었음.
# 항상 재확인 합시다 :)
import sys
input = sys.stdin.readline
def find(s):
    for st in adj_list[s]:
        if vis[st] == False:
            vis[st] = True
            known.add(st)
            find(st)

N, M = map(int, input().split())
T = list(map(int,input().split()))
knows = T[1:]
adj_list = [[] for _ in range(N+2)]
parties = [[] for _ in range(M+2)]
known = set()
for i in range(1, M+1):
    data = list(map(int, input().split()))
    parties[i].extend(data[1:])
    for idx in range(data[0]):
        for dt in data[1:]:
            for pt in data[1:]:
                if dt != pt and pt not in adj_list[dt]:
                    adj_list[dt].append(pt)
vis = [True]+([False]*N)
for i in knows:
    if vis[i] == False:
        known.add(i)
        vis[i] = True
        find(i)

for idx in range(1, M+1):
    for i in known:
        if i in parties[idx]:
            M -= 1
            break
print(M)
