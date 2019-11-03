'''
0 1 0 1
1 1 1 0
0 0 1 1
'''

result = []
for i in range(3):
    num = sum(list(map(int, input().split())))
    if num == 3:
        result.append('A')
    elif num == 2:
        result.append('B')
    elif num == 1:
        result.append('C')
    elif num == 0:
        result.append('D')
    elif num == 4:
        result.append('E')
for i in result:
    print(i)