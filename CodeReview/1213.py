import sys
sys.stdin = open('1213.txt', 'r')

def countString(a, b):
    cnt = 0
    while True:
        starting_i = a.find(b)
        if starting_i == -1:
            break
        a = a[starting_i+len(b):]
        cnt += 1
    return cnt

# print(countString(x, y))

for i in range(10):
    n = int(input())
    x = input()
    y = input()
    print(f'#{i+1} {countString(y, x)}')