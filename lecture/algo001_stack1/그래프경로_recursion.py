import sys
sys.stdin = open('stackinput.txt', 'r')

# 0번째 idx는 버린다.
# 이차원 배열을 만들어서 탐색
def search_myboard(start): # 행번호
    global result

    visited[start] = 1 # 방문한 곳은 1
    for next in range(1, mynode+1): # 시작노드에 등록된 도착노드 검색
        if myboard[start][next] == 1 and visited[next] == 0: # 안가본 길이면,
            # 멈춤조건
            if next == G:
                result = 1 # 갈 수 있는 곳
                return result # 검색중단

            # 재귀조건
            search_myboard(next) # 다음노드


for tc in range(1, int(input())+1):
    mynode, E = map(int, input().split())
    myboard = [[0] * (mynode+1) for _ in range((mynode+1))]

    # for r in myboard:
    #     print(r) # 1차원 배열로 확인해보기

    for _ in range(E):
        S, G = map(int, input().split()) # 출발 노드, 도착 노드
        myboard[S][G] = 1

    #print(myboard)
    S, G = map(int, input().split())
    visited = [0]*(mynode+1) # 방문한 곳 표시
    result = 0 # 갈 수 있으면 1, 갈 수 없으면  0

    search_myboard(S) # 재귀함수
    print(f'#{tc}', result)