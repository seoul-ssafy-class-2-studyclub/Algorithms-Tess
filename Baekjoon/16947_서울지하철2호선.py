import sys
sys.stdin = open('16947.txt', 'r')

'''
2개의 지선: 철도·수로 따위의 본선에서 갈려 나간 선.
1개의 순환

'''

N = int(input())

count = [0]*N
adj_list = [[] for _ in range(N)]
for _ in range(N):
    s, e = map(int, input().split())
    e = e-1
    s = s-1
    adj_list[s].append(e)
    adj_list[e].append(e)


