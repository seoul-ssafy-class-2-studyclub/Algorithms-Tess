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

    # 뒤에 2가 몇개가 나오던 상관없이 2만 나오면 계속 더해지는 중이였음(예상..)
    # 카운트 한번 되면 벗어나게 만들어야한다. 어떻게?


    '''
#7
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0 
0 0 0 0 1 2 2 
0 0 0 0 0 1 0 
0 0 2 1 0 2 1 
0 0 1 2 2 0 2 

    
    '''