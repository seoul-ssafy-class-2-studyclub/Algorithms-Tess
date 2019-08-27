import sys
sys.stdin = open('stackinput.txt', 'r')

# 0번째 idx는 버린다.
# 이차원 배열을 만들어서 탐색
def search_myboard(start):
    visited[start] = 1 # 방문한 곳은 1 

    pass




for tc in range(1, int(input())+1):
    mynode, E = map(int, input().split())
    myboard = [[0] * 100 for _ in range(100)]

    # for r in myboard:
    #     print(r) # 1차원 배열로 확인해보기

    for _ in range(E):
        S, G = map(int, input().split()) # 출발 노드, 도착 노드
        myboard[S][G] = 1

    print(myboard)
    S, G = map(int, input().split())
    visited = [0]*(myboard+1) # 방문한 곳 표시
    result = 0
    res = search_myboard(S) # 재귀함수