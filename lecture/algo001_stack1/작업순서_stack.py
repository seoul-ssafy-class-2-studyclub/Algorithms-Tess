# adj_arr
'''
9 9
4 1 1 2 2 3 2 7 5 6 7 6 1 5 8 5 8 9

#1 8 9 4 1 5 2 3 7 6
'''



T = 10
for tc in range(1, T+1):
    mynode, myline = map(int, input().split()) # 노드수, 간선수

    mymap = [ [0]*(mynode+1) for _ in range(mynode+1)]# 2차원 맵 생성

    # 간선정보입력
    data = list(map(int, input().split()))

    n = len(data)//2 # 나누기 결과는 실수 -> 정수로 변환
    for i in range(n):
        start = data[i*2] # 짝수
        end = data[i*2+1] # 홀수
        mymap[end][start] = 1 # 이렇게 사용하면 더 편해짐

    result = []
    while True:
        if len(result) == mynode: # 전체 노드가 경로에 모두 저장되면 탈출
            break
        start_col = []
        for col in range(1, len(mymap)): # 모든 칼럼을 검색
            if 1 not in mymap[col] and col not in result:
                start_col.append(col)

        for col in start_col:
            result.append(col) # 작업경로에 등록
            for row in range(len(mymap)):
                mymap[row][col] = 0 # 출발하는 노드로 연결되는 정보 삭제

    print(f'{tc}', end =' ')
    for i in result:
        print(i, end=' ')
    print()







