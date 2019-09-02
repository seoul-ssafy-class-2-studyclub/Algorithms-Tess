import sys
sys.stdin = open('6485.txt', 'r')


#
# my_dict = {'name': {'num': 0}}
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input()) # 버스 노선 수
#
#     avaliable = []
#     for _ in range(N):
#         A, B = map(int,input().split())
#         for a in range(A, B+1):
#             avaliable.append(a)
#
#     P = int(input())
#     for _ in range(P):
#         C = int(input())
#         my_dict[C] = {'num': 0}
#
#
#     for a in avaliable:
#         my_dict[a]['num'] += 1
#     print(f'#{tc}', end=' ')
#     for key, item in my_dict.items():
#         if my_dict[key]['num'] != 0:
#             print(my_dict[key]['num'], end=' ')
#     print()

## P개의 버스 정류장에 대해
## 각 정류장에 몇개의 버스 노선이 다니는가?


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 버스 노선 수

    # 위에서 선언하고 바로 계산하면 실행시간이 매우 단축된다.
    avaliable = [0] * 5001
    for _ in range(N):
        A, B = map(int,input().split())
        for a in range(A, B+1):
            avaliable[a] +=1

    stations = []
    P = int(input())
    for _ in range(P):
        C = int(input())
        stations.append(C)

    print(f'#{tc}', end=' ')
    for a in stations:
        print(avaliable[a], end=' ')
    print()
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input()) # 버스 노선 수
#
#     avaliable = []
#     for _ in range(N):
#         A, B = map(int,input().split())
#         avaliable.append([A, B, 0])
#
#     stations = []
#     P = int(input())
#     for _ in range(P):
#         C = int(input())
#         for i in range(C):
#             #print(i)
#             for idx in range(len(avaliable)):
#                 if avaliable[idx][0] <= i <= avaliable[idx][1]:
#                     avaliable[idx][2] += 1
#
#     print(f'#{tc}', end=' ')
#     for idx in range(len(avaliable)):
#         print(avaliable[idx][2], end=' ')
