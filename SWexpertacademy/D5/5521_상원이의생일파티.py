import sys
sys.stdin = open('5521.txt', 'r')


'''
disjoint-set

상원이의 생일 파티가 곧 열린다!
그렇기에 상원이는 반 친구들에게 생일 파티 초대장을 주려고 한다.
그러나 파티가 어색하게 되는 것을 원치 않는 상원이는 모든 친구들에게 초대장을 줄 생각이 없다.
같은 반에 있지만, 서로 친한 친구가 아닐 수도 있기 때문이다.
상원이는 우선 자신과 친한 친구들에게는 모두 초대장을 주기로 했다.
여기에 더해서 친한 친구의 친한 친구인 경우에도 초대장을 주기로 했다.
총 몇 명의 친구들에게 초대장을 주어야 하는지 구하는 프로그램을 작성하라.
상원이의 반에는 N명이 있으며, 각 학생들은 1번에서 N번까지의 번호가 붙어 있다.
여기서 1번 학생이 상원이다.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에 두 정수 N, M ( 2 ≤ N ≤ 500, 1 ≤ M ≤ 104 ) 이 공백으로 구분되어 주어진다.
M은 친한 친구 관계의 수 이다.
다음 M개의 줄의 각 줄에는 두 정수 a, b (1 ≤ a ＜ b ≤ N) 이 주어진다.
이는 a번 학생과 b번 학생이 서로 친한 친구 관계에 있다는 의미이다.

[출력]
각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 각 테스트 케이스마다 상원이의 생일 파티 초대장을 받는 친구의 수를 출력한다.
*상원이의 친구가 없을 수도 있다는 점에 유의해야 한다. 그리고 상원이는 초대장을 받는 사람에 속하지 않는다.


#1 0
#2 3

즉, visited를 체크하며 depth 2의 사람까지 초대장을 주겠다는 뜻과 같다.
반 전체 인원은 최대 500명이므로 서로의 관계를 나타내기 위한 500*500의 자료구조가 필요하다.
다음으로 친구 관계를 입력받으며 서로의 인덱스에 체크를 해준다.
그렇게 받은 입력을 통해 상원 - 친구 - 친구 까지만 탐색을 하며 visited를 체크하고
count를 늘려주면 끝나는 문제이다.
'''
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     # 서로 친하다 == 무방향이다
#     # 1번이 상원이 그러면 1번이 가진 자식들을 타고 자식과 자식을 타고 가야한다.
#     # 1번에 들어갈 자식이 없다면 아무도 없다는 뜻이다.
#     adj_list = [[] for _ in range(N+1)]
#     for _ in range(1, M+1):
#         a, b = map(int, input().split())
#         adj_list[a].append(b)
#         adj_list[b].append(a)
#     result = 0
#     visit = [False]*(N+1)
#     q = []
#     q.append((1, 0))
#     visit[1] = True
#
#     while q:
#         start, cnt = q.pop(0)
#
#         for child in adj_list[start]:
#             if visit[child] == False and cnt <= 1:
#                 visit[child] = True
#                 result += 1
#                 q.append((child, cnt+1))
#
#     print(f'#{tc}', result)
#



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N+1)]
    for _ in range(1, M+1):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    visited = [False] * (N+1)
    result = 0
    q = []
    visited[1] = True
    q.append((1, 0))
    while q:
        start, cnt = q.pop(0)
        for child in adj_list[start]:
            if visited[child] == False and cnt <= 1:
                visited[child] = True
                result += 1
                q.append((child, cnt+1))
    print(f'#{tc}', result)