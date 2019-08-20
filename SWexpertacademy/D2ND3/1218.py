import sys
sys.stdin = open('1218.txt', 'r')

standard = ['(', ')', '[', ']', '{', '}', '<', '>']
for tc in range(10):
    counting = [0] * 8
    length = int(input())
    A = list(map(str, input()))
    for i in range(8):
        if i%2 == 0:
            counting[i] = A.count(standard[i])
        if i%2 == 1:
            counting[i] = A.count(standard[i])
    res = 1
    for i in range(8):
        if i%2 == 0:
            if counting[i] != counting[i+1]:
                res = 0
    print(f'#{tc+1} {res}')