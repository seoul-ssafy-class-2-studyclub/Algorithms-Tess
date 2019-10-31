import sys
sys.stdin = open('10845.txt', 'r')

'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.


15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

1
2
2
0
1
2
-1
0
1
-1
0
3

'''

import sys
input = sys.stdin.readline
import collections
N = int(input()) # 명령의 수
q = collections.deque([])

for n in range(N):

    order = list(map(str, input().split()))

    if len(order) == 2:
        q.append(order[1])

    if order[0] == 'pop':
        if q:
            res = q.popleft()
            print(res)
        else:
            print(-1)

    if order[0] == 'size':
        print(len(q))

    if order[0] == 'empty':
        if q:
            print('0')
        else:
            print('1')

    if order[0] == 'front':
        if q:
            print(q[0])

        else:
            print('-1')

    if order[0] == 'back':
        if q:
            print(q[-1])
        else:
            print('-1')


