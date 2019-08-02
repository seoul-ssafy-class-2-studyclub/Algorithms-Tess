import sys
sys.stdin = open('7675.txt', 'r')

'''

2
2
Annyung Hasae Yo! LoL!
3
my name is Hye Soo. my id is Rhs0266. what your id Bro?


#1 3 0
#2 2 0 1
'''

p = ['.', '?', '!']
for case in range(1, int(input()) + 1): # 2
    count_list = [0] * int(input()) # 2 [0, 0] 인덱스에 나타난 이름 수를 더해줄 예정
    a = list(input().split())  # 'Annyung' 'Hasae' 'Yo!' 'LoL!'
    idx = 0
    for i in list(a):
        is_number = False
        for j in i:
            if j.isdigit():
                is_number = True
                break
        if not is_number and i.istitle():
            count_list[idx] += 1
        if i[-1] in p: # soo.
            idx += 1
    result = ' '.join(map(str, count_list))
    print(f'#{case} {result}')