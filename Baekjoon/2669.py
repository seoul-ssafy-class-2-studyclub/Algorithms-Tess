'''
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
'''

mat = []
for idx in range(4):
    new = list(map(int, input().split()))
    mat.append(new)

print(mat)


board = [[0]*100 for idx in range(100)]
print(board)


