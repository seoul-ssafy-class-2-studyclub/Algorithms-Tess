
def printArray(ary):
    print(ary)
    for i in ary:
        for j in i:
            print('%3d' % j, end=' ')
        print()


def snailArray(ary):
    offset = 0
    num = 1
    nrows = 5
    ncols = 5

    while nrows > 0 and ncols > 0:

        for i in range(offset, offset + ncols): # 0, 0+5
            ary[offset][i] = num # ary[0][0] = 1
            num += 1 # 2

        for i in range(offset + 1, offset + nrows):
            ary[i][offset + ncols - 1] = num
            num += 1

        for i in range(offset + ncols - 2, offset - 1, -1):
            ary[offset + nrows - 1][i] = num
            num += 1

        for i in range(offset + nrows - 2, offset, -1):
            ary[i][offset] = num
            num += 1

        offset += 1
        nrows -= 2
        ncols -= 2


ary = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

print(snailArray(ary))
print(printArray(ary))
