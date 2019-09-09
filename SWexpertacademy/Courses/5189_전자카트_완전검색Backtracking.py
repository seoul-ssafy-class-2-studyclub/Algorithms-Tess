import sys
sys.stdin = open('5189.txt', 'r')


# 백트레킹 문제인데, 회사 & 집 거리를 추가로 고려해줘야는 문제
# 추가로 시간 단축을 위해 프루닝 조건
# 거리를 계산하는 변수인 sub_result를 사용
# 이전 재귀로 돌아갈 때 기존 값을 빼주는 방식으로도 코드를 작성할 수도 있으며, 혹은 간단하게, 누적 값을 인자로 넘겨서도 풀 수 있다.
# 재귀 DFS

def DFS(start):
    global sub_result, result, final_result

    if len(sub_result) == N-1:
        for i, j in sub_result: # 조합 [(0, 1), (1, 2), (2, 3)]
            result += Battery[i][j]

        result += Battery[start][0]
        final_result.append(result)
        result = 0
        return

    for next in range(1, N):
        if not visited[next]: # False라면,
            sub_result.append((start, next))
            visited[next] = True
            DFS(next)
            sub_result.remove((start, next))
            visited[next] = False


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Battery = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sub_result =  [] #
    result = 0 #
    final_result =[] #
    DFS(0)

    print('#%d %d'%(tc, min(final_result)))