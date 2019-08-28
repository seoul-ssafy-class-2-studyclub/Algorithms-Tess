# 단계별로 값을 누적하여 누적한 값이 최소값보다 같거나 크면
# 다음단계로 안내려
def find_min(row):
    global submin, mymin

    # 재귀조건은 위에서 걸어야 한다.
    if submin > mymin: ### 0 > 9999...
        return # 누적중인 값이 최소값보다 크면 하위검색 중단

    if row == n: # 맨 아래까지 내려왔으면,
        if submin < mymin: # 누적값이 최소값보다 작으면 최소값 갱신
            mymin = submin
        # 더이상 내려가지 않고 반환
        return

    for x in range(n):
        if visited[x] == False: # False라면 들어갈 수 있는 것
            visited[x] = True
            submin += mymap[row][x] # 최소값 누적변수에 누적
            find_min(row+1) # 다음 열로 가면서 선택

            # 들어갔다 나왔으니 누적숫자만큼 뺀다.
            visited[x] = False
            submin -= mymin[row][x]

for tc in range(1, int(input())+1):
    n = int(input()) # 한변의 길이
    mymap = [ list(map(int, input().split())) for _ in range(n) ] # 2차원 배열
    visited = [False] * n # n개의 0을 가지는 배열
    mymin = 9999999 # 최소값 저장용
    submin = 0 # 중간 열별 값 저장용, 최소값보다 작으면 최소값에 저장
    find_min(0)
    print('#{} {}'.format(tc, mymin))

'''

선택된 부분의 값을 submin에 누적한다
row가 n이면 최소값과 비교를 한다.
누적 값이 최소값과 비교해서 커지면 더이상 처리하지 않는 식으로 진행

'''