'''
100

8
100 62 38 24 14 10 4 6
'''
res = 0
N = 100 # int(sys.stdin.readline())
stack = []
visit = []
stack.append(N)

start = [ _ for _ in range(N-1, -1, -1)]

print(start)

temp_result = []

while res > -1:
    for i in range(len(start)):
        if start[i] not in visit:
            res = stack.pop() - temp_result[-1]
            print(res)
            visit.append(start[i])
            temp_result.append(res)
            stack.append(res)

        elif start[i] in visit:
            break
print(temp_result)




