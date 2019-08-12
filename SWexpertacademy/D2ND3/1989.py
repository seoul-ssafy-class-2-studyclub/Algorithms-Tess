import sys
sys.stdin = open('1989.txt', 'r')


def Isitpalindrome(arr):
    if arr == arr[::-1]:
        return 1
    else:
        return 0

for tc in range(int(input())):
    text = list(map(str, input()))
    res = Isitpalindrome(text)
    print(f'#{tc+1} {res}')

