import sys
sys.stdin = open('2309.txt', 'r')

'''
일곱 난쟁이의 키의 합 100

input:

아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 
주어지는 키는 100을 넘지 않는 자연수

아홉 난쟁이의 키는 모두 다르며, 
가능한 정답이 여러 가지인 경우에는 아무거나 출력

output:

일곱 난쟁이의 키를 오름차순으로 출력


합이 100이 될 수 있는 후보들을 살려야함.
다 합치고, 두 개씩 빼가면서 100이 맞으면 됨
0,1
0,2 ... 8까지
1,2
1,2 ... 8까지

stack
'''


heights = [ int(input()) for _ in range(9) ]

# 9 명이니까 idx는 0~8까지 존재

total = 0

for _ in range(10):
    for ixo in range(8):
        if total == 100:
            res = heights
            break
        for ixs in range(ixo+1, 9):
            two = heights.pop(ixs)
            one = heights.pop(ixo)
            total = sum(heights)
            if total != 100:
                heights.insert(ixo, one)
                heights.insert(ixs, two)
            if total == 100:
                res = heights
                break

res = sorted(res)
for result in res:
    print(result)

