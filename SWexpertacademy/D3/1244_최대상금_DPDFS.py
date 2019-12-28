import sys
sys.stdin = open('1244.txt', 'r')

import itertools

def mymax(number, depth):
    global DP

    # 재귀의 trigger
    if depth == changeNum:
        return number

    # 가지치기
    if DP[depth].get(number) != None:
        res = DP[depth][number]
        return res

    # 자리바꾸기
    # 자리를 바꿀땐, list해서 넣어준다.
    res = 0
    for x, y in changeindexes:
        # 자리가 바뀌고,
        temp = changepositions(list(number), x, y)
        # 최종적으로 한 노드에서 6가지 경우의 수의 결과들중에 가장 맥스값을 찾는다
        res = max(res, int(mymax(temp, depth+1)))

    DP[depth][number] = res
    return res


# 자리 변경
def changepositions(arr, x, y):
    arr[x], arr[y] = arr[y], arr [x]
    arr = ''.join(arr)
    return arr


for tc in range(int(input())):

    candidate, changeNum = map(str, input().split())
    changeNum = int(changeNum)

    # 바꿀 경우의 수가 될 인덱스를 구한다.
    changeindexes = list(itertools.combinations([i for i in range(len(candidate))], 2))

    DP = [{} for _ in range(changeNum+1)]
    # 총 N만큼 바꿨을때, 나오는 결과값들중에 가장 max인 값을 구한다.
    # depth는 0 부터 시작해서 바꾸고, 바꾼 값들중에(6가지 경우의 수들중에) 가장 큰 res를 그 노드에 저장하는 식으로
    # 최대값을 끌어온다.
    # 같은 depth에서 같은 number인 경우, 가지치기가 가능하다.
    # depth가 changeNum만큼 되면 빠져나온다.
    print(f'#{tc+1}', mymax(candidate, 0))