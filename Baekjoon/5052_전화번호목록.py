'''
일관성 있는 목록인 경우에는 YES, 아닌 경우에는 NO를 출력한다.

NO
YES
'''

import sys
sys.stdin = open('5052.txt', 'r')



## 접두어가 겹치면 안된다
'''
97625999이 
97625999000의 접두어 이므로 NO가 된다.

앞에나온 모든 정보를 가지고
새로나온 정보에 대해서 check 한다.
'''

t = int(input())


for _ in range(t):
    n = int(input())

    save = []
    ans = 'YES'

    for i in range(n):
        data = input()
        save.append(data)

    check = [False]*n
    i = 0
    while save:

        cur = save[i]
        check[i] = True

        num = len(cur)
        nxt = save[i+1]

        print(cur, nxt)
        while cur != nxt[i+1][:num] and i+1 < n and check[i] == True:
            print(cur, nxt)
            save.append(nxt) # 같지않으면 다시 저장
            i += 1

        if i == n:
            break

    print(save)