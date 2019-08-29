board = [ [0]*100 for _ in range(100) ]

for _ in range(4):
    XF, YF, XS, YS = map(int, input().split())

    for col in range(YF, YS):
        for row in range(XF, XS):
            board[col][row] = 1
total = 0
for item in board:
    total += sum(item)
print(total)

'''
ROW 1부터 ROW 4까지 COL 2부터 COL 4까지
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
'''