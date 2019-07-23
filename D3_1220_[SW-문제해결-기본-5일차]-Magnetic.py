'''

board에서 열=같은행과 그다음열=같은행 for문을 중첩하여 1,2 pattern을 찾고,
count해주었다.

'''

for T in range(10):
    n = int(input())
    new_lists = []
    count = 0

    for t in range(n):
        new_lists.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            if new_lists[j][i] == 1:
                flag = 0
                for d in range(j+1, n):

                    if new_lists[d][i] == 1:
                        break
                    elif new_lists[d][i] == 2:
                        count += 1
                        flag += 1
                        if flag == 1:
                            break


    print(f'#{T+1} {count}')


    '''
Test    

#7
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0 
0 0 0 0 1 2 2 
0 0 0 0 0 1 0 
0 0 2 1 0 2 1 
0 0 1 2 2 0 2 

    
    '''