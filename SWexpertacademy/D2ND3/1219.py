import sys
sys.stdin = open('1219.txt', 'r')


## 이거 인접리스트로 바꿔보기!!
def gen():
    table = dict()
    t, e = map(int, input().split())
    #print(t, e)
    start = None

    for v in map(int, input().split()): # input을 받자마자 각 원소를 돈다.
        if start is None:
            start = v
        else:
            if str(start) in table:
                table[str(start)].append(str(v))
            else:
                table[str(start)] = [str(v)]

            start = None
    return t, table

def search(table):
    visited = [False]*100
    next_pos = table['0']
    while next_pos:
        pos = next_pos.pop()

        if visited[int(pos)]:
            continue

        else:
            add_next_pos = []
            if pos in table:
                add_next_pos = table[pos]
            if '99' in add_next_pos:
                #print(visited)
                return 1

            next_pos.extend(add_next_pos) # extend로 list 연결

    return 0 #모든 pos 를 순회했음에도 찾지 못했으므로 0 반환

#print(gen())
for tc in range(1,11):
    # tc 10개
    t, table = gen()
    print(f'#{t}', search(table))



