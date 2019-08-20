import sys
sys.stdin = open('1208.txt', 'r')

def mmax(arr):
    max_temp = arr[0]
    for i2 in range(1, len(arr)):
        if max_temp < arr[i2]:
            max_temp = arr[i2]
    return max_temp

def mmin(arr):
    min_temp = arr[0]
    for i3 in range(1, len(arr)):
        if min_temp > arr[i3]:
            min_temp = arr[i3]

    return min_temp


for tc in range(1, 11):
    numofdump = int(input())
    board = list(map(int, input().split()))
    for dump in range(numofdump): # dump : num of dump
        mmax1 = mmax(board) # max를 구한다
        mmin1 = mmin(board) # min을 구한다
        mmiddle = mmax1 - 1 # max-min을 해서 mmiddle을 구한다.
        mminidx = board.index(mmin1)
        mmaxidx = board.index(mmax1)
        board.pop(mminidx)
        board.insert(mminidx, mmin1 + 1)

        board.pop(mmaxidx)
        board.insert(mmaxidx, mmiddle)
        # 차이를 mmin1에 더하고, 반복한다.

    result = mmax(board) - mmin(board)
    print('#{} {}'.format(tc, result))
