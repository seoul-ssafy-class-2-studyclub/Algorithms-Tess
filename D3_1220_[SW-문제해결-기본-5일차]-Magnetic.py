'''

board에서 열=같은행과 그다음열=같은행 for문을 중첩하여 1,2 pattern을 찾고,
count해주었다.

'''

for T in range(10):
    n = int(input())
    new_lists = []
    count = 0

    for t in range(n):                          # board를 설정한다.
        new_lists.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
                                                # 1을 찾으면,
            if new_lists[j][i] == 1:
                flag = 0

                for d in range(j+1, n):         # 2를 찾기 시작하는데,
                    if new_lists[d][i] == 1:    # 1인 경우 빠져나와서 새로운 d를 받고,
                        break
                    elif new_lists[d][i] == 2:  # 2인 경우 (어차피 하나만 찾아도 패턴을 충족하므로)
                        count += 1              # count를 해주고,
                        flag += 1
                        if flag == 1:
                            break
                            '''
                            flag를 설정해서 2를 하나라도 발견하면 바로 나와서 
                            그 다음의 1부터 다시 시작하여 패턴을 찾도록 했다.

                            flag 설정 중요!
                            '''

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